# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..types.base_user import BaseUser
from .types.users_get_token_response import UsersGetTokenResponse
from .types.users_reset_token_response import UsersResetTokenResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class UsersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def reset_token(self, *, request_options: typing.Optional[RequestOptions] = None) -> UsersResetTokenResponse:
        """
        Reset the user token for the current user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersResetTokenResponse
            User token response

        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.users.reset_token()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/current-user/reset-token/", method="POST", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(UsersResetTokenResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_token(self, *, request_options: typing.Optional[RequestOptions] = None) -> UsersGetTokenResponse:
        """
        Get a user token to authenticate to the API as the current user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersGetTokenResponse
            User token response

        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.users.get_token()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/current-user/token", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(UsersGetTokenResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def whoami(self, *, request_options: typing.Optional[RequestOptions] = None) -> BaseUser:
        """
        Retrieve details of the account that you are using to access the API.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseUser


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.users.whoami()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/current-user/whoami", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(BaseUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[BaseUser]:
        """
        List the users that exist on the Label Studio server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BaseUser]


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.users.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/users/", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[BaseUser], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        id: typing.Optional[int] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        avatar: typing.Optional[str] = OMIT,
        initials: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        allow_newsletters: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseUser:
        """
        Create a user in Label Studio.

        Parameters
        ----------
        id : typing.Optional[int]
            User ID

        first_name : typing.Optional[str]
            First name of the user

        last_name : typing.Optional[str]
            Last name of the user

        username : typing.Optional[str]
            Username of the user

        email : typing.Optional[str]
            Email of the user

        avatar : typing.Optional[str]
            Avatar URL of the user

        initials : typing.Optional[str]
            Initials of the user

        phone : typing.Optional[str]
            Phone number of the user

        allow_newsletters : typing.Optional[bool]
            Whether the user allows newsletters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseUser


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.users.create()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/users/",
            method="POST",
            json={
                "id": id,
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "email": email,
                "avatar": avatar,
                "initials": initials,
                "phone": phone,
                "allow_newsletters": allow_newsletters,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(BaseUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> BaseUser:
        """
        Get info about a specific Label Studio user, based on the user ID.

        Parameters
        ----------
        id : int
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseUser


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.users.get(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/users/{jsonable_encoder(id)}/", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(BaseUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a specific Label Studio user.

        Parameters
        ----------
        id : int
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.users.delete(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/users/{jsonable_encoder(id)}/", method="DELETE", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        id: int,
        *,
        users_update_request_id: typing.Optional[int] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        avatar: typing.Optional[str] = OMIT,
        initials: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        allow_newsletters: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseUser:
        """
        Update details for a specific user, such as their name or contact information, in Label Studio.

        Parameters
        ----------
        id : int
            User ID

        users_update_request_id : typing.Optional[int]
            User ID

        first_name : typing.Optional[str]
            First name of the user

        last_name : typing.Optional[str]
            Last name of the user

        username : typing.Optional[str]
            Username of the user

        email : typing.Optional[str]
            Email of the user

        avatar : typing.Optional[str]
            Avatar URL of the user

        initials : typing.Optional[str]
            Initials of the user

        phone : typing.Optional[str]
            Phone number of the user

        allow_newsletters : typing.Optional[bool]
            Whether the user allows newsletters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseUser


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.users.update(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/users/{jsonable_encoder(id)}/",
            method="PATCH",
            json={
                "id": users_update_request_id,
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "email": email,
                "avatar": avatar,
                "initials": initials,
                "phone": phone,
                "allow_newsletters": allow_newsletters,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(BaseUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncUsersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def reset_token(self, *, request_options: typing.Optional[RequestOptions] = None) -> UsersResetTokenResponse:
        """
        Reset the user token for the current user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersResetTokenResponse
            User token response

        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.users.reset_token()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/current-user/reset-token/", method="POST", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(UsersResetTokenResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_token(self, *, request_options: typing.Optional[RequestOptions] = None) -> UsersGetTokenResponse:
        """
        Get a user token to authenticate to the API as the current user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UsersGetTokenResponse
            User token response

        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.users.get_token()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/current-user/token", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(UsersGetTokenResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def whoami(self, *, request_options: typing.Optional[RequestOptions] = None) -> BaseUser:
        """
        Retrieve details of the account that you are using to access the API.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseUser


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.users.whoami()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/current-user/whoami", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(BaseUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[BaseUser]:
        """
        List the users that exist on the Label Studio server.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BaseUser]


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.users.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/users/", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[BaseUser], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        id: typing.Optional[int] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        avatar: typing.Optional[str] = OMIT,
        initials: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        allow_newsletters: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseUser:
        """
        Create a user in Label Studio.

        Parameters
        ----------
        id : typing.Optional[int]
            User ID

        first_name : typing.Optional[str]
            First name of the user

        last_name : typing.Optional[str]
            Last name of the user

        username : typing.Optional[str]
            Username of the user

        email : typing.Optional[str]
            Email of the user

        avatar : typing.Optional[str]
            Avatar URL of the user

        initials : typing.Optional[str]
            Initials of the user

        phone : typing.Optional[str]
            Phone number of the user

        allow_newsletters : typing.Optional[bool]
            Whether the user allows newsletters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseUser


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.users.create()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/users/",
            method="POST",
            json={
                "id": id,
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "email": email,
                "avatar": avatar,
                "initials": initials,
                "phone": phone,
                "allow_newsletters": allow_newsletters,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(BaseUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> BaseUser:
        """
        Get info about a specific Label Studio user, based on the user ID.

        Parameters
        ----------
        id : int
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseUser


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.users.get(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/users/{jsonable_encoder(id)}/", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(BaseUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a specific Label Studio user.

        Parameters
        ----------
        id : int
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.users.delete(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/users/{jsonable_encoder(id)}/", method="DELETE", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        id: int,
        *,
        users_update_request_id: typing.Optional[int] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        username: typing.Optional[str] = OMIT,
        email: typing.Optional[str] = OMIT,
        avatar: typing.Optional[str] = OMIT,
        initials: typing.Optional[str] = OMIT,
        phone: typing.Optional[str] = OMIT,
        allow_newsletters: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BaseUser:
        """
        Update details for a specific user, such as their name or contact information, in Label Studio.

        Parameters
        ----------
        id : int
            User ID

        users_update_request_id : typing.Optional[int]
            User ID

        first_name : typing.Optional[str]
            First name of the user

        last_name : typing.Optional[str]
            Last name of the user

        username : typing.Optional[str]
            Username of the user

        email : typing.Optional[str]
            Email of the user

        avatar : typing.Optional[str]
            Avatar URL of the user

        initials : typing.Optional[str]
            Initials of the user

        phone : typing.Optional[str]
            Phone number of the user

        allow_newsletters : typing.Optional[bool]
            Whether the user allows newsletters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BaseUser


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.users.update(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/users/{jsonable_encoder(id)}/",
            method="PATCH",
            json={
                "id": users_update_request_id,
                "first_name": first_name,
                "last_name": last_name,
                "username": username,
                "email": email,
                "avatar": avatar,
                "initials": initials,
                "phone": phone,
                "allow_newsletters": allow_newsletters,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(BaseUser, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
