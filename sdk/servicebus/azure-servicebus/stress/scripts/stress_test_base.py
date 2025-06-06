# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

import time
import threading
from datetime import datetime, timedelta
import concurrent
import sys
import os
import asyncio
import logging

try:
    import psutil
except ImportError:
    pass  # If psutil isn't installed, simply does not capture process stats.

from azure.servicebus import ServiceBusMessage, ServiceBusMessageBatch
from azure.servicebus.exceptions import MessageAlreadySettled

from logger import get_logger
from app_insights_metric import AbstractMonitorMetric
from process_monitor import ProcessMonitor

PRINT_CONSOLE = True
LOGFILE_NAME = os.environ.get("DEBUG_SHARE") + "output"


class ReceiveType:
    push = "push"
    pull = "pull"
    none = None


class StressTestResults(object):
    def __init__(self):
        self.total_sent = 0
        self.total_received = 0
        self.time_elapsed = None
        self.state_by_sender = {}
        self.state_by_receiver = {}
        self.actual_size = 0

    def __repr__(self):
        return str(vars(self))


class StressTestRunnerState(object):
    """Per-runner state, e.g. if you spawn 3 senders each will have this as their state object,
    which will be coalesced at completion into StressTestResults"""

    def __init__(self):
        self.total_sent = 0
        self.total_received = 0
        self.cpu_percent = None
        self.memory_bytes = None
        self.timestamp = None
        self.exceptions = []

    def __repr__(self):
        return str(vars(self))

    def populate_process_stats(self, monitor):
        self.timestamp = datetime.utcnow()
        try:
            self.cpu_percent = psutil.cpu_percent()
            self.memory_bytes = psutil.virtual_memory().percent
        except NameError:
            return  # psutil was not installed, fall back to simply not capturing these stats.


class StressTestRunner:
    """Framework for running a service bus stress test.
    Duration can be overriden via the --stress_test_duration flag from the command line"""

    def __init__(
        self,
        senders,
        receivers,
        admin_client,
        duration=timedelta(minutes=15),
        receive_type=ReceiveType.push,
        send_batch_size=None,
        message_size=10,
        max_wait_time=10,
        send_delay=1.0,
        receive_delay=0,
        should_complete_messages=True,
        max_message_count=10,
        send_session_id=None,
        fail_on_exception=True,
        azure_monitor_metric=None,
        process_monitor=None,
        logging_level=logging.ERROR,
        transport_type=False,
        rotating_logs=True,
    ):
        self.senders = senders
        self.receivers = receivers
        self.admin_client = admin_client
        self.duration = duration
        self.receive_type = receive_type
        self.message_size = message_size
        self.send_batch_size = send_batch_size
        self.max_wait_time = max_wait_time
        self.send_delay = send_delay
        self.receive_delay = receive_delay
        self.should_complete_messages = should_complete_messages
        self.max_message_count = max_message_count
        self.fail_on_exception = fail_on_exception
        self.send_session_id = send_session_id
        self.azure_monitor_metric = azure_monitor_metric or AbstractMonitorMetric("fake_test_name")
        self.logging_level = logging_level
        self.rotating_logs = rotating_logs
        logfile_name = LOGFILE_NAME
        if transport_type:
            logfile_name += "_ws.log"
        else:
            logfile_name += ".log"
        self.logger = get_logger(logfile_name, "stress_test", self.logging_level, rotating_logs=self.rotating_logs)
        self.process_monitor = process_monitor or ProcessMonitor(
            "monitor_{}".format(logfile_name),
            "stress_test_queues",
            print_console=PRINT_CONSOLE,
        )

        # Because of pickle we need to create a state object and not just pass around ourselves.
        # If we ever require multiple runs of this one after another, just make Run() reset this.
        self._state = StressTestRunnerState()

        self._duration_override = None
        for arg in sys.argv:
            if arg.startswith("--duration="):
                self._duration_override = timedelta(seconds=int(arg.split("=")[1]))

        self._should_stop = False

    # Plugin functions the caller can override to further tailor the test.
    def on_send(self, state, sent_message, sender):
        """Called on every successful send, per message"""
        pass

    def on_receive(self, state, received_message, receiver):
        """Called on every successful receive, per message"""
        pass

    def on_receive_batch(self, state, batch, receiver):
        """Called on every successful receive, at the batch or iterator level rather than per-message"""
        pass

    def post_receive(self, state, receiver):
        """Called after completion of every successful receive"""
        pass

    def on_complete(self, send_results=[], receive_results=[]):
        """Called on stress test run completion"""
        pass

    def pre_process_message(self, message):
        """Allows user to transform the message before batching or sending it."""
        pass

    def pre_process_message_batch(self, message):
        """Allows user to transform the batch before sending it."""
        pass

    def pre_process_message_body(self, payload):
        """Allows user to transform message payload before sending it."""
        return payload

    def _schedule_interval_logger(self, end_time, logger, process_monitor, description="", interval_seconds=300):
        def _do_interval_logging():
            if end_time > datetime.utcnow() and not self._should_stop:
                self._state.populate_process_stats(process_monitor)
                logger.critical("%s RECURRENT STATUS: %s", description, self._state)
                self._schedule_interval_logger(end_time, logger, process_monitor, description, interval_seconds)

        t = threading.Timer(interval_seconds, _do_interval_logging)
        t.start()

    def _construct_message(self):
        if self.send_batch_size != None:
            batch = ServiceBusMessageBatch()
            for _ in range(self.send_batch_size):
                message = ServiceBusMessage(self.pre_process_message_body("a" * self.message_size))
                self.pre_process_message(message)
                batch.add_message(message)
            self.pre_process_message_batch(batch)
            return batch
        else:
            message = ServiceBusMessage(self.pre_process_message_body("a" * self.message_size))
            self.pre_process_message(message)
            return message

    def _send(self, sender, end_time):
        self._schedule_interval_logger(end_time, self.logger, self.process_monitor, "Sender " + str(self))
        try:
            self.logger.debug("Starting send loop")
            # log sender
            self.logger.debug("Sender: %s", sender)
            with sender:
                while end_time > datetime.utcnow() and not self._should_stop:
                    try:
                        message = self._construct_message()
                        if self.send_session_id != None:
                            message.session_id = self.send_session_id
                        self.logger.debug("Sending message: %s", message)
                        sender.send_messages(message)
                        self.azure_monitor_metric.record_messages_cpu_memory(
                            self.send_batch_size,
                            self.process_monitor.cpu_usage_percent,
                            self.process_monitor.memory_usage_percent,
                        )
                        if self.send_batch_size:
                            self._state.total_sent += self.send_batch_size
                        else:
                            self._state.total_sent += 1  # send single message
                        self.on_send(self._state, message, sender)

                    except Exception as e:
                        self.logger.exception("Exception during send: %s", e)
                        self.azure_monitor_metric.record_error(e)
                        self._state.exceptions.append(e)
                        if self.fail_on_exception:
                            raise
                    time.sleep(self.send_delay)
            self._state.timestamp = datetime.utcnow()
            return self._state
        except Exception as e:
            self.logger.exception("Exception in sender: %s", e)
            self._should_stop = True
            raise

    def _receive(self, receiver, end_time):
        self._schedule_interval_logger(end_time, self.logger, self.process_monitor, "Receiver " + str(self))
        # log receiver
        self.logger.debug("Receiver: %s", receiver)
        try:
            with receiver:
                while end_time > datetime.utcnow() and not self._should_stop:
                    try:
                        if self.receive_type == ReceiveType.pull:
                            batch = receiver.receive_messages(
                                max_message_count=self.max_message_count,
                                max_wait_time=self.max_wait_time,
                            )
                        elif self.receive_type == ReceiveType.push:
                            receiver.max_wait_time = self.max_wait_time
                            batch = receiver
                        # else:
                        #     batch = []

                        for message in batch:
                            # log reciever
                            self.logger.debug("Received message: %s", message)
                            self.on_receive(self._state, message, receiver)
                            try:
                                if self.should_complete_messages:
                                    receiver.complete_message(message)
                            except MessageAlreadySettled:  # It may have been settled in the plugin callback.
                                pass

                            self._state.total_received += 1
                            # TODO: Get EnqueuedTimeUtc out of broker properties and calculate latency. Should properties/app properties be mostly None?
                            if end_time <= datetime.utcnow():
                                break
                            time.sleep(self.receive_delay)
                            self.azure_monitor_metric.record_messages_cpu_memory(
                                1,
                                self.process_monitor.cpu_usage_percent,
                                self.process_monitor.memory_usage_percent,
                            )
                        self.post_receive(self._state, receiver)
                    except Exception as e:
                        self.logger.exception("Exception during receive: %s", e)
                        self._state.exceptions.append(e)
                        self.azure_monitor_metric.record_error(e)
                        if self.fail_on_exception:
                            raise
                self._state.timestamp = datetime.utcnow()
            return self._state
        except Exception as e:
            self.azure_monitor_metric.record_error(e)
            self.logger.exception("Exception in receiver %s", e)
            self._should_stop = True
            raise

    def run(self):

        start_time = datetime.utcnow()
        if isinstance(self.duration, int):
            self.duration = timedelta(seconds=self.duration)
        end_time = start_time + (self._duration_override or self.duration)

        with self.process_monitor:
            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as proc_pool:
                self.logger.info("STARTING PROC POOL")
                if self.senders:
                    senders = [proc_pool.submit(self._send, sender, end_time) for sender in self.senders]
                else:
                    senders = []
                if self.receivers:
                    receivers = [proc_pool.submit(self._receive, receiver, end_time) for receiver in self.receivers]
                else:
                    receivers = []
                result = StressTestResults()
                for each in concurrent.futures.as_completed(senders + receivers):
                    self.logger.info("SOMETHING FINISHED")
                    if each in senders:
                        result.state_by_sender[each] = each.result()
                    if each in receivers:
                        result.state_by_receiver[each] = each.result()
                # TODO: do as_completed in one batch to provide a way to short-circuit on failure.
                if self.senders:
                    result.state_by_sender = {
                        s: f.result() for s, f in zip(self.senders, concurrent.futures.as_completed(senders))
                    }
                    result.total_sent = sum([r.total_sent for r in result.state_by_sender.values()])
                if self.receivers:
                    result.state_by_receiver = {
                        r: f.result() for r, f in zip(self.receivers, concurrent.futures.as_completed(receivers))
                    }
                    self.logger.info("Got receiver results")
                    result.total_received = sum([r.total_received for r in result.state_by_receiver.values()])
                result.time_elapsed = end_time - start_time
                self.logger.critical("Stress test completed.  Results:\n %s", result)
                return result


class StressTestRunnerAsync(StressTestRunner):
    def __init__(
        self,
        senders,
        receivers,
        duration=timedelta(minutes=15),
        admin_client=None,
        receive_type=ReceiveType.push,
        send_batch_size=None,
        message_size=10,
        max_wait_time=10,
        send_delay=1.00,
        receive_delay=0,
        should_complete_messages=True,
        max_message_count=1,
        send_session_id=None,
        fail_on_exception=True,
        azure_monitor_metric=None,
        process_monitor=None,
        logging_level=logging.ERROR,
        transport_type=False,
        rotating_logs=True,
    ):
        super(StressTestRunnerAsync, self).__init__(
            senders,
            receivers,
            duration=duration,
            admin_client=admin_client,
            receive_type=receive_type,
            send_batch_size=send_batch_size,
            message_size=message_size,
            max_wait_time=max_wait_time,
            send_delay=send_delay,
            receive_delay=receive_delay,
            should_complete_messages=should_complete_messages,
            max_message_count=max_message_count,
            send_session_id=send_session_id,
            fail_on_exception=fail_on_exception,
            azure_monitor_metric=azure_monitor_metric,
            process_monitor=process_monitor,
            logging_level=logging_level,
            transport_type=transport_type,
            rotating_logs=rotating_logs,
        )

    async def _send_async(self, sender, end_time):
        self._schedule_interval_logger(end_time, self.logger, self.process_monitor, "Sender " + str(self))
        try:
            async with sender:
                while end_time > datetime.utcnow() and not self._should_stop:
                    try:
                        message = self._construct_message()
                        if self.send_session_id != None:
                            message.session_id = self.send_session_id
                        await sender.send_messages(message)
                        self.azure_monitor_metric.record_messages_cpu_memory(
                            self.send_batch_size,
                            self.process_monitor.cpu_usage_percent,
                            self.process_monitor.memory_usage_percent,
                        )
                        if self.send_batch_size:
                            self._state.total_sent += self.send_batch_size
                        else:
                            self._state.total_sent += 1
                        self.on_send(self._state, message, sender)
                    except Exception as e:
                        self.logger.exception("Exception during send: %s", e)
                        self.azure_monitor_metric.record_error(e)
                        self._state.exceptions.append(e)
                        if self.fail_on_exception:
                            raise
                    await asyncio.sleep(self.send_delay)
            self._state.timestamp = datetime.utcnow()
            return self._state
        except Exception as e:
            self.logger.exception("Exception in sender: %s", e)
            self._should_stop = True
            raise

    async def _receive_handle_message(self, message, receiver, end_time):
        self.on_receive(self._state, message, receiver)
        try:
            if self.should_complete_messages:
                await receiver.complete_message(message)
        except MessageAlreadySettled:  # It may have been settled in the plugin callback.
            pass
        self._state.total_received += 1
        # TODO: Get EnqueuedTimeUtc out of broker properties and calculate latency. Should properties/app properties be mostly None?
        await asyncio.sleep(self.receive_delay)
        self.azure_monitor_metric.record_messages_cpu_memory(
            1,
            self.process_monitor.cpu_usage_percent,
            self.process_monitor.memory_usage_percent,
        )

    async def _receive_async(self, receiver, end_time):
        self._schedule_interval_logger(end_time, self.logger, self.process_monitor, "Receiver " + str(self))
        try:
            async with receiver:
                while end_time > datetime.utcnow() and not self._should_stop:
                    try:
                        if self.receive_type == ReceiveType.pull:
                            batch = await receiver.receive_messages(
                                max_message_count=self.max_message_count,
                                max_wait_time=self.max_wait_time,
                            )
                            for message in batch:
                                await self._receive_handle_message(message, receiver, end_time)
                        elif self.receive_type == ReceiveType.push:
                            receiver.max_wait_time = self.max_wait_time
                            batch = receiver
                            async for message in batch:
                                if end_time <= datetime.utcnow():
                                    break
                                await self._receive_handle_message(message, receiver, end_time)
                        self.post_receive(self._state, receiver)
                    except Exception as e:
                        self.logger.exception("Exception during receive: %s", e)
                        self._state.exceptions.append(e)
                        self.azure_monitor_metric.record_error(e)
                        if self.fail_on_exception:
                            raise
            self._state.timestamp = datetime.utcnow()
            return self._state
        except Exception as e:
            self.azure_monitor_metric.record_error(e)
            self.logger.exception("Exception in receiver %s", e)
            self._should_stop = True
            raise

    async def run_async(self):
        start_time = datetime.utcnow()
        if isinstance(self.duration, int):
            self.duration = timedelta(seconds=self.duration)
        end_time = start_time + (self._duration_override or self.duration)
        if self.senders:
            send_tasks = [asyncio.create_task(self._send_async(sender, end_time)) for sender in self.senders]
        else:
            send_tasks = []
        if self.receivers:
            receive_tasks = [
                asyncio.create_task(self._receive_async(receiver, end_time)) for receiver in self.receivers
            ]
        else:
            receive_tasks = []
        with self.process_monitor:
            # await asyncio.gather(*send_tasks, *receive_tasks)
            for task in asyncio.as_completed(send_tasks + receive_tasks):
                try:
                    await task
                except Exception as e:
                    print(e)
            result = StressTestResults()
            if self.senders:
                result.state_by_sender = {s: f.result() for s, f in zip(self.senders, send_tasks)}
                result.total_sent = sum([r.total_sent for r in result.state_by_sender.values()])
            if self.receivers:
                result.state_by_receiver = {r: f.result() for r, f in zip(self.receivers, receive_tasks)}
                self.logger.info("got receiver results")

                result.total_received = sum([r.total_received for r in result.state_by_receiver.values()])
            result.time_elapsed = end_time - start_time
            self.logger.critical("Stress test completed.  Results:\n%s", result)
            return result
