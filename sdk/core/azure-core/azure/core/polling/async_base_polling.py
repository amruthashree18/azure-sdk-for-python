# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------
from typing import TypeVar, cast, Union
from ..exceptions import HttpResponseError
from .base_polling import (
    _failed,
    BadStatus,
    BadResponse,
    OperationFailed,
    _SansIOLROBasePolling,
    _raise_if_bad_http_status_and_method,
)
from ._async_poller import AsyncPollingMethod
from ..pipeline._tools import is_rest
from .. import AsyncPipelineClient
from ..pipeline import PipelineResponse
from ..pipeline.transport import (
    HttpRequest as LegacyHttpRequest,
    AsyncHttpTransport,
    AsyncHttpResponse as LegacyAsyncHttpResponse,
)
from ..rest import HttpRequest, AsyncHttpResponse

HttpRequestType = Union[LegacyHttpRequest, HttpRequest]
AsyncHttpResponseType = Union[LegacyAsyncHttpResponse, AsyncHttpResponse]
HttpRequestTypeVar = TypeVar("HttpRequestTypeVar", bound=HttpRequestType)
AsyncHttpResponseTypeVar = TypeVar("AsyncHttpResponseTypeVar", bound=AsyncHttpResponseType)


PollingReturnType_co = TypeVar("PollingReturnType_co", covariant=True)

__all__ = ["AsyncLROBasePolling"]


class AsyncLROBasePolling(
    _SansIOLROBasePolling[
        PollingReturnType_co,
        AsyncPipelineClient[HttpRequestTypeVar, AsyncHttpResponseTypeVar],
        HttpRequestTypeVar,
        AsyncHttpResponseTypeVar,
    ],
    AsyncPollingMethod[PollingReturnType_co],
):
    """A base LRO async poller.

    This assumes a basic flow:
    - I analyze the response to decide the polling approach
    - I poll
    - I ask the final resource depending of the polling approach

    If your polling need are more specific, you could implement a PollingMethod directly
    """

    _initial_response: PipelineResponse[HttpRequestTypeVar, AsyncHttpResponseTypeVar]
    """Store the initial response."""

    _pipeline_response: PipelineResponse[HttpRequestTypeVar, AsyncHttpResponseTypeVar]
    """Store the latest received HTTP response, initialized by the first answer."""

    @property
    def _transport(
        self,
    ) -> AsyncHttpTransport[HttpRequestTypeVar, AsyncHttpResponseTypeVar]:
        return self._client._pipeline._transport  # pylint: disable=protected-access

    async def run(self) -> None:
        try:
            await self._poll()

        except BadStatus as err:
            self._status = "Failed"
            raise HttpResponseError(response=self._pipeline_response.http_response, error=err) from err

        except BadResponse as err:
            self._status = "Failed"
            raise HttpResponseError(
                response=self._pipeline_response.http_response,
                message=str(err),
                error=err,
            ) from err

        except OperationFailed as err:
            raise HttpResponseError(response=self._pipeline_response.http_response, error=err) from err

    async def _poll(self) -> None:
        """Poll status of operation so long as operation is incomplete and
        we have an endpoint to query.

        :raises ~azure.core.polling.base_polling.OperationFailed: If operation status 'Failed' or 'Canceled'.
        :raises ~azure.core.polling.base_polling.BadStatus: If response status invalid.
        :raises ~azure.core.polling.base_polling.BadResponse: If response invalid.
        """
        if not self.finished():
            await self.update_status()
        while not self.finished():
            await self._delay()
            await self.update_status()

        if _failed(self.status()):
            raise OperationFailed("Operation failed or canceled")

        final_get_url = self._operation.get_final_get_url(self._pipeline_response)
        if final_get_url:
            self._pipeline_response = await self.request_status(final_get_url)
            _raise_if_bad_http_status_and_method(self._pipeline_response.http_response)

    async def _sleep(self, delay: float) -> None:
        await self._transport.sleep(delay)

    async def _delay(self) -> None:
        """Check for a 'retry-after' header to set timeout,
        otherwise use configured timeout.
        """
        delay = self._extract_delay()
        await self._sleep(delay)

    async def update_status(self) -> None:
        """Update the current status of the LRO."""
        self._pipeline_response = await self.request_status(self._operation.get_polling_url())
        _raise_if_bad_http_status_and_method(self._pipeline_response.http_response)
        self._status = self._operation.get_status(self._pipeline_response)

    async def request_status(self, status_link: str) -> PipelineResponse[HttpRequestTypeVar, AsyncHttpResponseTypeVar]:
        """Do a simple GET to this status link.

        This method re-inject 'x-ms-client-request-id'.

        :param str status_link: URL to poll.
        :rtype: azure.core.pipeline.PipelineResponse
        :return: The response of the status request.
        """
        if self._path_format_arguments:
            status_link = self._client.format_url(status_link, **self._path_format_arguments)
        # Re-inject 'x-ms-client-request-id' while polling
        if "request_id" not in self._operation_config:
            self._operation_config["request_id"] = self._get_request_id()

        if is_rest(self._initial_response.http_response):
            rest_request = cast(HttpRequestTypeVar, HttpRequest("GET", status_link))
            # Need a cast, as "_return_pipeline_response" mutate the return type, and that return type is not
            # declared in the typing of "send_request"
            return cast(
                PipelineResponse[HttpRequestTypeVar, AsyncHttpResponseTypeVar],
                await self._client.send_request(rest_request, _return_pipeline_response=True, **self._operation_config),
            )

        # Legacy HttpRequest and AsyncHttpResponse from azure.core.pipeline.transport
        # casting things here, as we don't want the typing system to know
        # about the legacy APIs.
        request = cast(HttpRequestTypeVar, self._client.get(status_link))
        return cast(
            PipelineResponse[HttpRequestTypeVar, AsyncHttpResponseTypeVar],
            await self._client._pipeline.run(  # pylint: disable=protected-access
                request, stream=False, **self._operation_config
            ),
        )


__all__ = ["AsyncLROBasePolling"]
