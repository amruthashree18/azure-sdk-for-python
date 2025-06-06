# pylint: disable=line-too-long,useless-suppression
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential

from azure.mgmt.recoveryservicessiterecovery import SiteRecoveryManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-recoveryservicessiterecovery
# USAGE
    python replication_protection_intents_create.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = SiteRecoveryManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="509099b2-9d2c-4636-b43e-bd5cafb6be69",
        resource_group_name="resourceGroupPS1",
        resource_name="vault1",
    )

    response = client.replication_protection_intents.create(
        intent_object_name="vm1",
        input={
            "properties": {
                "providerSpecificDetails": {
                    "fabricObjectId": "/subscriptions/509099b2-9d2c-4636-b43e-bd5cafb6be69/resourceGroups/removeOne/providers/Microsoft.Compute/virtualMachines/vmPpgAv5",
                    "instanceType": "A2A",
                    "primaryLocation": "eastUs2",
                    "recoveryAvailabilityType": "Single",
                    "recoveryLocation": "westus2",
                    "recoveryResourceGroupId": "/subscriptions/509099b2-9d2c-4636-b43e-bd5cafb6be69/resourceGroups/removeOne-asr",
                    "recoverySubscriptionId": "ed5bcdf6-d61e-47bd-8ea9-f2bd379a2640",
                }
            }
        },
    )
    print(response)


# x-ms-original-file: specification/recoveryservicessiterecovery/resource-manager/Microsoft.RecoveryServices/stable/2025-01-01/examples/ReplicationProtectionIntents_Create.json
if __name__ == "__main__":
    main()
