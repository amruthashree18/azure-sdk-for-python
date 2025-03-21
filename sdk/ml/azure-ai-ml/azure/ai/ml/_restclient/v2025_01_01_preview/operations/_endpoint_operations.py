# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING

from msrest import Serializer

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling

from .. import models as _models
from .._vendor import _convert_request, _format_url_section

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Iterable, Optional, TypeVar, Union
    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False
# fmt: off

def build_list_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2025-01-01-preview")  # type: str
    endpoint_type = kwargs.pop('endpoint_type', None)  # type: Optional[Union[str, "_models.EndpointType"]]
    include_online_endpoints = kwargs.pop('include_online_endpoints', False)  # type: Optional[bool]
    include_serverless_endpoints = kwargs.pop('include_serverless_endpoints', False)  # type: Optional[bool]
    include_connections = kwargs.pop('include_connections', False)  # type: Optional[bool]
    skip = kwargs.pop('skip', None)  # type: Optional[str]
    expand = kwargs.pop('expand', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/endpoints")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str', pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]{2,32}$'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')
    if endpoint_type is not None:
        _query_parameters['endpointType'] = _SERIALIZER.query("endpoint_type", endpoint_type, 'str')
    if include_online_endpoints is not None:
        _query_parameters['includeOnlineEndpoints'] = _SERIALIZER.query("include_online_endpoints", include_online_endpoints, 'bool')
    if include_serverless_endpoints is not None:
        _query_parameters['includeServerlessEndpoints'] = _SERIALIZER.query("include_serverless_endpoints", include_serverless_endpoints, 'bool')
    if include_connections is not None:
        _query_parameters['includeConnections'] = _SERIALIZER.query("include_connections", include_connections, 'bool')
    if skip is not None:
        _query_parameters['$skip'] = _SERIALIZER.query("skip", skip, 'str')
    if expand is not None:
        _query_parameters['$expand'] = _SERIALIZER.query("expand", expand, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_get_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    endpoint_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2025-01-01-preview")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/endpoints/{endpointName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str', pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]{2,32}$'),
        "endpointName": _SERIALIZER.url("endpoint_name", endpoint_name, 'str', pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]{2,32}$'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_create_or_update_request_initial(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    endpoint_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2025-01-01-preview")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/endpoints/{endpointName}")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str', pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]{2,32}$'),
        "endpointName": _SERIALIZER.url("endpoint_name", endpoint_name, 'str', pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]{2,32}$'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PUT",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_list_keys_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    endpoint_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2025-01-01-preview")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/endpoints/{endpointName}/listKeys")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str', pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]{2,32}$'),
        "endpointName": _SERIALIZER.url("endpoint_name", endpoint_name, 'str', pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]{2,32}$'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_get_models_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    endpoint_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2025-01-01-preview")  # type: str

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/endpoints/{endpointName}/models")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str', pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]{2,32}$'),
        "endpointName": _SERIALIZER.url("endpoint_name", endpoint_name, 'str', pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]{2,32}$'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )


def build_regenerate_keys_request(
    subscription_id,  # type: str
    resource_group_name,  # type: str
    workspace_name,  # type: str
    endpoint_name,  # type: str
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    api_version = kwargs.pop('api_version', "2025-01-01-preview")  # type: str
    content_type = kwargs.pop('content_type', None)  # type: Optional[str]

    accept = "application/json"
    # Construct URL
    _url = kwargs.pop("template_url", "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/endpoints/{endpointName}/regenerateKey")  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, 'str', min_length=1),
        "resourceGroupName": _SERIALIZER.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1),
        "workspaceName": _SERIALIZER.url("workspace_name", workspace_name, 'str', pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_-]{2,32}$'),
        "endpointName": _SERIALIZER.url("endpoint_name", endpoint_name, 'str', pattern=r'^[a-zA-Z0-9][a-zA-Z0-9_.-]{2,32}$'),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    _query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    _header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        _header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    _header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=_url,
        params=_query_parameters,
        headers=_header_parameters,
        **kwargs
    )

# fmt: on
class EndpointOperations(object):
    """EndpointOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.machinelearningservices.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace
    def list(
        self,
        resource_group_name,  # type: str
        workspace_name,  # type: str
        endpoint_type=None,  # type: Optional[Union[str, "_models.EndpointType"]]
        include_online_endpoints=False,  # type: Optional[bool]
        include_serverless_endpoints=False,  # type: Optional[bool]
        include_connections=False,  # type: Optional[bool]
        skip=None,  # type: Optional[str]
        expand=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.EndpointResourcePropertiesBasicResourceArmPaginatedResult"]
        """List All the endpoints under this workspace.

        List All the endpoints under this workspace.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param workspace_name: Azure Machine Learning Workspace Name.
        :type workspace_name: str
        :param endpoint_type: Endpoint type filter.
        :type endpoint_type: str or ~azure.mgmt.machinelearningservices.models.EndpointType
        :param include_online_endpoints:
        :type include_online_endpoints: bool
        :param include_serverless_endpoints:
        :type include_serverless_endpoints: bool
        :param include_connections:
        :type include_connections: bool
        :param skip: Continuation token for pagination.
        :type skip: str
        :param expand: Whether the endpoint resource will be expand to include deployment information,
         e.g. $expand=deployments.
        :type expand: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either
         EndpointResourcePropertiesBasicResourceArmPaginatedResult or the result of cls(response)
        :rtype:
         ~azure.core.paging.ItemPaged[~azure.mgmt.machinelearningservices.models.EndpointResourcePropertiesBasicResourceArmPaginatedResult]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2025-01-01-preview")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.EndpointResourcePropertiesBasicResourceArmPaginatedResult"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    api_version=api_version,
                    endpoint_type=endpoint_type,
                    include_online_endpoints=include_online_endpoints,
                    include_serverless_endpoints=include_serverless_endpoints,
                    include_connections=include_connections,
                    skip=skip,
                    expand=expand,
                    template_url=self.list.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_list_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    api_version=api_version,
                    endpoint_type=endpoint_type,
                    include_online_endpoints=include_online_endpoints,
                    include_serverless_endpoints=include_serverless_endpoints,
                    include_connections=include_connections,
                    skip=skip,
                    expand=expand,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("EndpointResourcePropertiesBasicResourceArmPaginatedResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    list.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/endpoints"}  # type: ignore

    @distributed_trace
    def get(
        self,
        resource_group_name,  # type: str
        workspace_name,  # type: str
        endpoint_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.EndpointResourcePropertiesBasicResource"
        """Gets endpoint resource.

        Gets endpoint resource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param workspace_name: Azure Machine Learning Workspace Name.
        :type workspace_name: str
        :param endpoint_name: Name of the endpoint resource.
        :type endpoint_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EndpointResourcePropertiesBasicResource, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.EndpointResourcePropertiesBasicResource
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.EndpointResourcePropertiesBasicResource"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2025-01-01-preview")  # type: str

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            endpoint_name=endpoint_name,
            api_version=api_version,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('EndpointResourcePropertiesBasicResource', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/endpoints/{endpointName}"}  # type: ignore


    def _create_or_update_initial(
        self,
        resource_group_name,  # type: str
        workspace_name,  # type: str
        endpoint_name,  # type: str
        body,  # type: "_models.EndpointResourcePropertiesBasicResource"
        **kwargs  # type: Any
    ):
        # type: (...) -> Optional["_models.EndpointResourcePropertiesBasicResource"]
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.EndpointResourcePropertiesBasicResource"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2025-01-01-preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(body, 'EndpointResourcePropertiesBasicResource')

        request = build_create_or_update_request_initial(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            endpoint_name=endpoint_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self._create_or_update_initial.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response, error_format=ARMErrorFormat)

        deserialized = None
        response_headers = {}
        if response.status_code == 200:
            deserialized = self._deserialize('EndpointResourcePropertiesBasicResource', pipeline_response)

        if response.status_code == 202:
            response_headers['Location']=self._deserialize('str', response.headers.get('Location'))
            response_headers['Retry-After']=self._deserialize('int', response.headers.get('Retry-After'))
            

        if cls:
            return cls(pipeline_response, deserialized, response_headers)

        return deserialized

    _create_or_update_initial.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/endpoints/{endpointName}"}  # type: ignore


    @distributed_trace
    def begin_create_or_update(
        self,
        resource_group_name,  # type: str
        workspace_name,  # type: str
        endpoint_name,  # type: str
        body,  # type: "_models.EndpointResourcePropertiesBasicResource"
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["_models.EndpointResourcePropertiesBasicResource"]
        """Create or update endpoint resource with the specified parameters.

        Create or update endpoint resource with the specified parameters.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param workspace_name: Azure Machine Learning Workspace Name.
        :type workspace_name: str
        :param endpoint_name: Name of the endpoint resource.
        :type endpoint_name: str
        :param body: Endpoint resource object.
        :type body: ~azure.mgmt.machinelearningservices.models.EndpointResourcePropertiesBasicResource
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: By default, your polling method will be ARMPolling. Pass in False for this
         operation to not poll, or pass in your own initialized polling object for a personal polling
         strategy.
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
         Retry-After header is present.
        :return: An instance of LROPoller that returns either EndpointResourcePropertiesBasicResource
         or the result of cls(response)
        :rtype:
         ~azure.core.polling.LROPoller[~azure.mgmt.machinelearningservices.models.EndpointResourcePropertiesBasicResource]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2025-01-01-preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]
        polling = kwargs.pop('polling', True)  # type: Union[bool, PollingMethod]
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.EndpointResourcePropertiesBasicResource"]
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token', None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_or_update_initial(
                resource_group_name=resource_group_name,
                workspace_name=workspace_name,
                endpoint_name=endpoint_name,
                body=body,
                api_version=api_version,
                content_type=content_type,
                cls=lambda x,y,z: x,
                **kwargs
            )
        kwargs.pop('error_map', None)

        def get_long_running_output(pipeline_response):
            response = pipeline_response.http_response
            deserialized = self._deserialize('EndpointResourcePropertiesBasicResource', pipeline_response)
            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized


        if polling is True: polling_method = ARMPolling(lro_delay, lro_options={'final-state-via': 'location'}, **kwargs)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)

    begin_create_or_update.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/endpoints/{endpointName}"}  # type: ignore

    @distributed_trace
    def list_keys(
        self,
        resource_group_name,  # type: str
        workspace_name,  # type: str
        endpoint_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.EndpointKeys"
        """List keys for the endpoint resource.

        List keys for the endpoint resource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param workspace_name: Azure Machine Learning Workspace Name.
        :type workspace_name: str
        :param endpoint_name: Name of the endpoint resource.
        :type endpoint_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: EndpointKeys, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.EndpointKeys
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.EndpointKeys"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2025-01-01-preview")  # type: str

        
        request = build_list_keys_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            endpoint_name=endpoint_name,
            api_version=api_version,
            template_url=self.list_keys.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('EndpointKeys', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    list_keys.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/endpoints/{endpointName}/listKeys"}  # type: ignore


    @distributed_trace
    def get_models(
        self,
        resource_group_name,  # type: str
        workspace_name,  # type: str
        endpoint_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["_models.EndpointModels"]
        """Get available models under the endpoint resource.

        Get available models under the endpoint resource.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param workspace_name: Azure Machine Learning Workspace Name.
        :type workspace_name: str
        :param endpoint_name: Name of the endpoint resource.
        :type endpoint_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either EndpointModels or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.machinelearningservices.models.EndpointModels]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        api_version = kwargs.pop('api_version', "2025-01-01-preview")  # type: str

        cls = kwargs.pop('cls', None)  # type: ClsType["_models.EndpointModels"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        def prepare_request(next_link=None):
            if not next_link:
                
                request = build_get_models_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    endpoint_name=endpoint_name,
                    api_version=api_version,
                    template_url=self.get_models.metadata['url'],
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)

            else:
                
                request = build_get_models_request(
                    subscription_id=self._config.subscription_id,
                    resource_group_name=resource_group_name,
                    workspace_name=workspace_name,
                    endpoint_name=endpoint_name,
                    api_version=api_version,
                    template_url=next_link,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("EndpointModels", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
                request,
                stream=False,
                **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response


        return ItemPaged(
            get_next, extract_data
        )
    get_models.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/endpoints/{endpointName}/models"}  # type: ignore

    @distributed_trace
    def regenerate_keys(
        self,
        resource_group_name,  # type: str
        workspace_name,  # type: str
        endpoint_name,  # type: str
        body,  # type: "_models.RegenerateServiceAccountKeyContent"
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.AccountApiKeys"
        """Regenerate account keys.

        Regenerate account keys.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
        :type resource_group_name: str
        :param workspace_name: Azure Machine Learning Workspace Name.
        :type workspace_name: str
        :param endpoint_name: Name of the endpoint resource.
        :type endpoint_name: str
        :param body:
        :type body: ~azure.mgmt.machinelearningservices.models.RegenerateServiceAccountKeyContent
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: AccountApiKeys, or the result of cls(response)
        :rtype: ~azure.mgmt.machinelearningservices.models.AccountApiKeys
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.AccountApiKeys"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2025-01-01-preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(body, 'RegenerateServiceAccountKeyContent')

        request = build_regenerate_keys_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
            endpoint_name=endpoint_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.regenerate_keys.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('AccountApiKeys', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    regenerate_keys.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.MachineLearningServices/workspaces/{workspaceName}/endpoints/{endpointName}/regenerateKey"}  # type: ignore

