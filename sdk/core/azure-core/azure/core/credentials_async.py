# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from __future__ import annotations
from types import TracebackType
from typing import Any, Optional, AsyncContextManager, Type, Union, TYPE_CHECKING
from typing_extensions import Protocol, runtime_checkable

if TYPE_CHECKING:
    from .credentials import AccessToken, AccessTokenInfo, TokenRequestOptions


@runtime_checkable
class AsyncTokenCredential(Protocol, AsyncContextManager["AsyncTokenCredential"]):
    """Protocol for classes able to provide OAuth tokens."""

    async def get_token(
        self,
        *scopes: str,
        claims: Optional[str] = None,
        tenant_id: Optional[str] = None,
        enable_cae: bool = False,
        **kwargs: Any,
    ) -> AccessToken:
        """Request an access token for `scopes`.

        :param str scopes: The type of access needed.

        :keyword str claims: Additional claims required in the token, such as those returned in a resource
            provider's claims challenge following an authorization failure.
        :keyword str tenant_id: Optional tenant to include in the token request.
        :keyword bool enable_cae: Indicates whether to enable Continuous Access Evaluation (CAE) for the requested
            token. Defaults to False.

        :rtype: AccessToken
        :return: An AccessToken instance containing the token string and its expiration time in Unix time.
        """
        ...

    async def close(self) -> None:
        """Close the credential, releasing any resources.

        :return: None
        :rtype: None
        """

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ) -> None:
        pass


@runtime_checkable
class AsyncSupportsTokenInfo(Protocol, AsyncContextManager["AsyncSupportsTokenInfo"]):
    """Protocol for classes able to provide OAuth access tokens with additional properties."""

    async def get_token_info(self, *scopes: str, options: Optional[TokenRequestOptions] = None) -> AccessTokenInfo:
        """Request an access token for `scopes`.

        This is an alternative to `get_token` to enable certain scenarios that require additional properties
        on the token.

        :param str scopes: The type of access needed.
        :keyword options: A dictionary of options for the token request. Unknown options will be ignored. Optional.
        :paramtype options: TokenRequestOptions

        :rtype: AccessTokenInfo
        :return: An AccessTokenInfo instance containing the token string and its expiration time in Unix time.
        """
        ...

    async def close(self) -> None:
        """Close the credential, releasing any resources.

        :return: None
        :rtype: None
        """

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ) -> None:
        pass


AsyncTokenProvider = Union[AsyncTokenCredential, AsyncSupportsTokenInfo]
