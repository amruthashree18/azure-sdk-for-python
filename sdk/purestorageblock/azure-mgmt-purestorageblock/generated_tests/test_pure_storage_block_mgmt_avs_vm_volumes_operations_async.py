# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.purestorageblock.aio import PureStorageBlockMgmtClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer
from devtools_testutils.aio import recorded_by_proxy_async

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestPureStorageBlockMgmtAvsVmVolumesOperationsAsync(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(PureStorageBlockMgmtClient, is_async=True)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_avs_vm_volumes_begin_update(self, resource_group):
        response = await (
            await self.client.avs_vm_volumes.begin_update(
                resource_group_name=resource_group.name,
                storage_pool_name="str",
                avs_vm_id="str",
                volume_id="str",
                properties={"properties": {"softDeletion": {"destroyed": bool, "eradicationTimestamp": "str"}}},
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_avs_vm_volumes_get(self, resource_group):
        response = await self.client.avs_vm_volumes.get(
            resource_group_name=resource_group.name,
            storage_pool_name="str",
            avs_vm_id="str",
            volume_id="str",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_avs_vm_volumes_begin_delete(self, resource_group):
        response = await (
            await self.client.avs_vm_volumes.begin_delete(
                resource_group_name=resource_group.name,
                storage_pool_name="str",
                avs_vm_id="str",
                volume_id="str",
            )
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy_async
    async def test_avs_vm_volumes_list_by_avs_vm(self, resource_group):
        response = self.client.avs_vm_volumes.list_by_avs_vm(
            resource_group_name=resource_group.name,
            storage_pool_name="str",
            avs_vm_id="str",
        )
        result = [r async for r in response]
        # please add some check logic here by yourself
        # ...
