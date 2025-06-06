# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from azure.mgmt.network import NetworkManagementClient

from devtools_testutils import AzureMgmtRecordedTestCase, RandomNameResourceGroupPreparer, recorded_by_proxy

AZURE_LOCATION = "eastus"


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestNetworkManagementVirtualNetworkGatewayConnectionsOperations(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(NetworkManagementClient)

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_virtual_network_gateway_connections_begin_create_or_update(self, resource_group):
        response = self.client.virtual_network_gateway_connections.begin_create_or_update(
            resource_group_name=resource_group.name,
            virtual_network_gateway_connection_name="str",
            parameters={
                "connectionType": "str",
                "virtualNetworkGateway1": {
                    "activeActive": bool,
                    "adminState": "str",
                    "allowRemoteVnetTraffic": bool,
                    "allowVirtualWanTraffic": bool,
                    "autoScaleConfiguration": {"bounds": {"max": 0, "min": 0}},
                    "bgpSettings": {
                        "asn": 0,
                        "bgpPeeringAddress": "str",
                        "bgpPeeringAddresses": [
                            {
                                "customBgpIpAddresses": ["str"],
                                "defaultBgpIpAddresses": ["str"],
                                "ipconfigurationId": "str",
                                "tunnelIpAddresses": ["str"],
                            }
                        ],
                        "peerWeight": 0,
                    },
                    "customRoutes": {
                        "addressPrefixes": ["str"],
                        "ipamPoolPrefixAllocations": [
                            {"allocatedAddressPrefixes": ["str"], "id": "str", "numberOfIpAddresses": "str"}
                        ],
                    },
                    "disableIPSecReplayProtection": bool,
                    "enableBgp": bool,
                    "enableBgpRouteTranslationForNat": bool,
                    "enableDnsForwarding": bool,
                    "enableHighBandwidthVpnGateway": bool,
                    "enablePrivateIpAddress": bool,
                    "etag": "str",
                    "extendedLocation": {"name": "str", "type": "str"},
                    "gatewayDefaultSite": {"id": "str"},
                    "gatewayType": "str",
                    "id": "str",
                    "identity": {
                        "principalId": "str",
                        "tenantId": "str",
                        "type": "str",
                        "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                    },
                    "inboundDnsForwardingEndpoint": "str",
                    "ipConfigurations": [
                        {
                            "etag": "str",
                            "id": "str",
                            "name": "str",
                            "privateIPAddress": "str",
                            "privateIPAllocationMethod": "str",
                            "provisioningState": "str",
                            "publicIPAddress": {"id": "str"},
                            "subnet": {"id": "str"},
                        }
                    ],
                    "location": "str",
                    "name": "str",
                    "natRules": [
                        {
                            "etag": "str",
                            "externalMappings": [{"addressSpace": "str", "portRange": "str"}],
                            "id": "str",
                            "internalMappings": [{"addressSpace": "str", "portRange": "str"}],
                            "ipConfigurationId": "str",
                            "mode": "str",
                            "name": "str",
                            "provisioningState": "str",
                            "type": "str",
                        }
                    ],
                    "provisioningState": "str",
                    "resiliencyModel": "str",
                    "resourceGuid": "str",
                    "sku": {"capacity": 0, "name": "str", "tier": "str"},
                    "tags": {"str": "str"},
                    "type": "str",
                    "vNetExtendedLocationResourceId": "str",
                    "virtualNetworkGatewayMigrationStatus": {"errorMessage": "str", "phase": "str", "state": "str"},
                    "virtualNetworkGatewayPolicyGroups": [
                        {
                            "etag": "str",
                            "id": "str",
                            "isDefault": bool,
                            "name": "str",
                            "policyMembers": [{"attributeType": "str", "attributeValue": "str", "name": "str"}],
                            "priority": 0,
                            "provisioningState": "str",
                            "vngClientConnectionConfigurations": [{"id": "str"}],
                        }
                    ],
                    "vpnClientConfiguration": {
                        "aadAudience": "str",
                        "aadIssuer": "str",
                        "aadTenant": "str",
                        "radiusServerAddress": "str",
                        "radiusServerSecret": "str",
                        "radiusServers": [
                            {"radiusServerAddress": "str", "radiusServerScore": 0, "radiusServerSecret": "str"}
                        ],
                        "vngClientConnectionConfigurations": [
                            {
                                "etag": "str",
                                "id": "str",
                                "name": "str",
                                "provisioningState": "str",
                                "virtualNetworkGatewayPolicyGroups": [{"id": "str"}],
                                "vpnClientAddressPool": {
                                    "addressPrefixes": ["str"],
                                    "ipamPoolPrefixAllocations": [
                                        {"allocatedAddressPrefixes": ["str"], "id": "str", "numberOfIpAddresses": "str"}
                                    ],
                                },
                            }
                        ],
                        "vpnAuthenticationTypes": ["str"],
                        "vpnClientAddressPool": {
                            "addressPrefixes": ["str"],
                            "ipamPoolPrefixAllocations": [
                                {"allocatedAddressPrefixes": ["str"], "id": "str", "numberOfIpAddresses": "str"}
                            ],
                        },
                        "vpnClientIpsecPolicies": [
                            {
                                "dhGroup": "str",
                                "ikeEncryption": "str",
                                "ikeIntegrity": "str",
                                "ipsecEncryption": "str",
                                "ipsecIntegrity": "str",
                                "pfsGroup": "str",
                                "saDataSizeKilobytes": 0,
                                "saLifeTimeSeconds": 0,
                            }
                        ],
                        "vpnClientProtocols": ["str"],
                        "vpnClientRevokedCertificates": [
                            {"etag": "str", "id": "str", "name": "str", "provisioningState": "str", "thumbprint": "str"}
                        ],
                        "vpnClientRootCertificates": [
                            {
                                "publicCertData": "str",
                                "etag": "str",
                                "id": "str",
                                "name": "str",
                                "provisioningState": "str",
                            }
                        ],
                    },
                    "vpnGatewayGeneration": "str",
                    "vpnType": "str",
                },
                "authorizationKey": "str",
                "connectionMode": "str",
                "connectionProtocol": "str",
                "connectionStatus": "str",
                "dpdTimeoutSeconds": 0,
                "egressBytesTransferred": 0,
                "egressNatRules": [{"id": "str"}],
                "enableBgp": bool,
                "enablePrivateLinkFastPath": bool,
                "etag": "str",
                "expressRouteGatewayBypass": bool,
                "gatewayCustomBgpIpAddresses": [{"customBgpIpAddress": "str", "ipConfigurationId": "str"}],
                "id": "str",
                "ingressBytesTransferred": 0,
                "ingressNatRules": [{"id": "str"}],
                "ipsecPolicies": [
                    {
                        "dhGroup": "str",
                        "ikeEncryption": "str",
                        "ikeIntegrity": "str",
                        "ipsecEncryption": "str",
                        "ipsecIntegrity": "str",
                        "pfsGroup": "str",
                        "saDataSizeKilobytes": 0,
                        "saLifeTimeSeconds": 0,
                    }
                ],
                "localNetworkGateway2": {
                    "bgpSettings": {
                        "asn": 0,
                        "bgpPeeringAddress": "str",
                        "bgpPeeringAddresses": [
                            {
                                "customBgpIpAddresses": ["str"],
                                "defaultBgpIpAddresses": ["str"],
                                "ipconfigurationId": "str",
                                "tunnelIpAddresses": ["str"],
                            }
                        ],
                        "peerWeight": 0,
                    },
                    "etag": "str",
                    "fqdn": "str",
                    "gatewayIpAddress": "str",
                    "id": "str",
                    "localNetworkAddressSpace": {
                        "addressPrefixes": ["str"],
                        "ipamPoolPrefixAllocations": [
                            {"allocatedAddressPrefixes": ["str"], "id": "str", "numberOfIpAddresses": "str"}
                        ],
                    },
                    "location": "str",
                    "name": "str",
                    "provisioningState": "str",
                    "resourceGuid": "str",
                    "tags": {"str": "str"},
                    "type": "str",
                },
                "location": "str",
                "name": "str",
                "peer": {"id": "str"},
                "provisioningState": "str",
                "resourceGuid": "str",
                "routingWeight": 0,
                "sharedKey": "str",
                "tags": {"str": "str"},
                "trafficSelectorPolicies": [{"localAddressRanges": ["str"], "remoteAddressRanges": ["str"]}],
                "tunnelConnectionStatus": [
                    {
                        "connectionStatus": "str",
                        "egressBytesTransferred": 0,
                        "ingressBytesTransferred": 0,
                        "lastConnectionEstablishedUtcTime": "str",
                        "tunnel": "str",
                    }
                ],
                "tunnelProperties": [{"bgpPeeringAddress": "str", "tunnelIpAddress": "str"}],
                "type": "str",
                "useLocalAzureIpAddress": bool,
                "usePolicyBasedTrafficSelectors": bool,
                "virtualNetworkGateway2": {
                    "activeActive": bool,
                    "adminState": "str",
                    "allowRemoteVnetTraffic": bool,
                    "allowVirtualWanTraffic": bool,
                    "autoScaleConfiguration": {"bounds": {"max": 0, "min": 0}},
                    "bgpSettings": {
                        "asn": 0,
                        "bgpPeeringAddress": "str",
                        "bgpPeeringAddresses": [
                            {
                                "customBgpIpAddresses": ["str"],
                                "defaultBgpIpAddresses": ["str"],
                                "ipconfigurationId": "str",
                                "tunnelIpAddresses": ["str"],
                            }
                        ],
                        "peerWeight": 0,
                    },
                    "customRoutes": {
                        "addressPrefixes": ["str"],
                        "ipamPoolPrefixAllocations": [
                            {"allocatedAddressPrefixes": ["str"], "id": "str", "numberOfIpAddresses": "str"}
                        ],
                    },
                    "disableIPSecReplayProtection": bool,
                    "enableBgp": bool,
                    "enableBgpRouteTranslationForNat": bool,
                    "enableDnsForwarding": bool,
                    "enableHighBandwidthVpnGateway": bool,
                    "enablePrivateIpAddress": bool,
                    "etag": "str",
                    "extendedLocation": {"name": "str", "type": "str"},
                    "gatewayDefaultSite": {"id": "str"},
                    "gatewayType": "str",
                    "id": "str",
                    "identity": {
                        "principalId": "str",
                        "tenantId": "str",
                        "type": "str",
                        "userAssignedIdentities": {"str": {"clientId": "str", "principalId": "str"}},
                    },
                    "inboundDnsForwardingEndpoint": "str",
                    "ipConfigurations": [
                        {
                            "etag": "str",
                            "id": "str",
                            "name": "str",
                            "privateIPAddress": "str",
                            "privateIPAllocationMethod": "str",
                            "provisioningState": "str",
                            "publicIPAddress": {"id": "str"},
                            "subnet": {"id": "str"},
                        }
                    ],
                    "location": "str",
                    "name": "str",
                    "natRules": [
                        {
                            "etag": "str",
                            "externalMappings": [{"addressSpace": "str", "portRange": "str"}],
                            "id": "str",
                            "internalMappings": [{"addressSpace": "str", "portRange": "str"}],
                            "ipConfigurationId": "str",
                            "mode": "str",
                            "name": "str",
                            "provisioningState": "str",
                            "type": "str",
                        }
                    ],
                    "provisioningState": "str",
                    "resiliencyModel": "str",
                    "resourceGuid": "str",
                    "sku": {"capacity": 0, "name": "str", "tier": "str"},
                    "tags": {"str": "str"},
                    "type": "str",
                    "vNetExtendedLocationResourceId": "str",
                    "virtualNetworkGatewayMigrationStatus": {"errorMessage": "str", "phase": "str", "state": "str"},
                    "virtualNetworkGatewayPolicyGroups": [
                        {
                            "etag": "str",
                            "id": "str",
                            "isDefault": bool,
                            "name": "str",
                            "policyMembers": [{"attributeType": "str", "attributeValue": "str", "name": "str"}],
                            "priority": 0,
                            "provisioningState": "str",
                            "vngClientConnectionConfigurations": [{"id": "str"}],
                        }
                    ],
                    "vpnClientConfiguration": {
                        "aadAudience": "str",
                        "aadIssuer": "str",
                        "aadTenant": "str",
                        "radiusServerAddress": "str",
                        "radiusServerSecret": "str",
                        "radiusServers": [
                            {"radiusServerAddress": "str", "radiusServerScore": 0, "radiusServerSecret": "str"}
                        ],
                        "vngClientConnectionConfigurations": [
                            {
                                "etag": "str",
                                "id": "str",
                                "name": "str",
                                "provisioningState": "str",
                                "virtualNetworkGatewayPolicyGroups": [{"id": "str"}],
                                "vpnClientAddressPool": {
                                    "addressPrefixes": ["str"],
                                    "ipamPoolPrefixAllocations": [
                                        {"allocatedAddressPrefixes": ["str"], "id": "str", "numberOfIpAddresses": "str"}
                                    ],
                                },
                            }
                        ],
                        "vpnAuthenticationTypes": ["str"],
                        "vpnClientAddressPool": {
                            "addressPrefixes": ["str"],
                            "ipamPoolPrefixAllocations": [
                                {"allocatedAddressPrefixes": ["str"], "id": "str", "numberOfIpAddresses": "str"}
                            ],
                        },
                        "vpnClientIpsecPolicies": [
                            {
                                "dhGroup": "str",
                                "ikeEncryption": "str",
                                "ikeIntegrity": "str",
                                "ipsecEncryption": "str",
                                "ipsecIntegrity": "str",
                                "pfsGroup": "str",
                                "saDataSizeKilobytes": 0,
                                "saLifeTimeSeconds": 0,
                            }
                        ],
                        "vpnClientProtocols": ["str"],
                        "vpnClientRevokedCertificates": [
                            {"etag": "str", "id": "str", "name": "str", "provisioningState": "str", "thumbprint": "str"}
                        ],
                        "vpnClientRootCertificates": [
                            {
                                "publicCertData": "str",
                                "etag": "str",
                                "id": "str",
                                "name": "str",
                                "provisioningState": "str",
                            }
                        ],
                    },
                    "vpnGatewayGeneration": "str",
                    "vpnType": "str",
                },
            },
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_virtual_network_gateway_connections_get(self, resource_group):
        response = self.client.virtual_network_gateway_connections.get(
            resource_group_name=resource_group.name,
            virtual_network_gateway_connection_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_virtual_network_gateway_connections_begin_delete(self, resource_group):
        response = self.client.virtual_network_gateway_connections.begin_delete(
            resource_group_name=resource_group.name,
            virtual_network_gateway_connection_name="str",
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_virtual_network_gateway_connections_begin_update_tags(self, resource_group):
        response = self.client.virtual_network_gateway_connections.begin_update_tags(
            resource_group_name=resource_group.name,
            virtual_network_gateway_connection_name="str",
            parameters={"tags": {"str": "str"}},
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_virtual_network_gateway_connections_begin_set_shared_key(self, resource_group):
        response = self.client.virtual_network_gateway_connections.begin_set_shared_key(
            resource_group_name=resource_group.name,
            virtual_network_gateway_connection_name="str",
            parameters={"value": "str", "id": "str"},
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_virtual_network_gateway_connections_get_shared_key(self, resource_group):
        response = self.client.virtual_network_gateway_connections.get_shared_key(
            resource_group_name=resource_group.name,
            virtual_network_gateway_connection_name="str",
            api_version="2024-07-01",
        )

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_virtual_network_gateway_connections_list(self, resource_group):
        response = self.client.virtual_network_gateway_connections.list(
            resource_group_name=resource_group.name,
            api_version="2024-07-01",
        )
        result = [r for r in response]
        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_virtual_network_gateway_connections_begin_reset_shared_key(self, resource_group):
        response = self.client.virtual_network_gateway_connections.begin_reset_shared_key(
            resource_group_name=resource_group.name,
            virtual_network_gateway_connection_name="str",
            parameters={"keyLength": 0},
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_virtual_network_gateway_connections_begin_start_packet_capture(self, resource_group):
        response = self.client.virtual_network_gateway_connections.begin_start_packet_capture(
            resource_group_name=resource_group.name,
            virtual_network_gateway_connection_name="str",
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_virtual_network_gateway_connections_begin_stop_packet_capture(self, resource_group):
        response = self.client.virtual_network_gateway_connections.begin_stop_packet_capture(
            resource_group_name=resource_group.name,
            virtual_network_gateway_connection_name="str",
            parameters={"sasUrl": "str"},
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_virtual_network_gateway_connections_begin_get_ike_sas(self, resource_group):
        response = self.client.virtual_network_gateway_connections.begin_get_ike_sas(
            resource_group_name=resource_group.name,
            virtual_network_gateway_connection_name="str",
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...

    @RandomNameResourceGroupPreparer(location=AZURE_LOCATION)
    @recorded_by_proxy
    def test_virtual_network_gateway_connections_begin_reset_connection(self, resource_group):
        response = self.client.virtual_network_gateway_connections.begin_reset_connection(
            resource_group_name=resource_group.name,
            virtual_network_gateway_connection_name="str",
            api_version="2024-07-01",
        ).result()  # call '.result()' to poll until service return final result

        # please add some check logic here by yourself
        # ...
