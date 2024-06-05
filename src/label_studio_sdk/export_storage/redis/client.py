# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.request_options import RequestOptions
from ...types.redis_export_storage import RedisExportStorage
from .types.redis_create_response import RedisCreateResponse
from .types.redis_update_response import RedisUpdateResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RedisClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, project: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RedisExportStorage]:
        """
        Get a list of all Redis export storage connections.

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RedisExportStorage]


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.export_storage.redis.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/storages/export/redis", method="GET", params={"project": project}, request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[RedisExportStorage], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        project: typing.Optional[int] = OMIT,
        path: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        port: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        db: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RedisCreateResponse:
        """
        Create a new Redis export storage connection to store annotations.

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        path : typing.Optional[str]
            Storage prefix (optional)

        host : typing.Optional[str]
            Server Host IP (optional)

        port : typing.Optional[str]
            Server Port (optional)

        password : typing.Optional[str]
            Server Password (optional)

        db : typing.Optional[int]
            Database ID of database to use

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedisCreateResponse


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.export_storage.redis.create()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/storages/export/redis",
            method="POST",
            json={"project": project, "path": path, "host": host, "port": port, "password": password, "db": db},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RedisCreateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def validate(self, *, request_options: typing.Optional[RequestOptions] = None) -> RedisExportStorage:
        """
        Validate a specific Redis export storage connection.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedisExportStorage


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.export_storage.redis.validate()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/storages/export/redis/validate", method="POST", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RedisExportStorage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> RedisExportStorage:
        """
        Get a specific Redis export storage connection.

        Parameters
        ----------
        id : int
            A unique integer value identifying this redis export storage.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedisExportStorage


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.export_storage.redis.get(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/export/redis/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RedisExportStorage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a specific Redis export storage connection.

        Parameters
        ----------
        id : int
            A unique integer value identifying this redis export storage.

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
        client.export_storage.redis.delete(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/export/redis/{jsonable_encoder(id)}", method="DELETE", request_options=request_options
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
        project: typing.Optional[int] = OMIT,
        path: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        port: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        db: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RedisUpdateResponse:
        """
        Update a specific Redis export storage connection.

        Parameters
        ----------
        id : int
            A unique integer value identifying this redis export storage.

        project : typing.Optional[int]
            Project ID

        path : typing.Optional[str]
            Storage prefix (optional)

        host : typing.Optional[str]
            Server Host IP (optional)

        port : typing.Optional[str]
            Server Port (optional)

        password : typing.Optional[str]
            Server Password (optional)

        db : typing.Optional[int]
            Database ID of database to use

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedisUpdateResponse


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.export_storage.redis.update(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/export/redis/{jsonable_encoder(id)}",
            method="PATCH",
            json={"project": project, "path": path, "host": host, "port": port, "password": password, "db": db},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RedisUpdateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def sync(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RedisExportStorage:
        """
        Sync tasks from a specific Redis export storage connection.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedisExportStorage


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.export_storage.redis.sync(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/export/redis/{jsonable_encoder(id)}/sync", method="POST", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RedisExportStorage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncRedisClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, project: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RedisExportStorage]:
        """
        Get a list of all Redis export storage connections.

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RedisExportStorage]


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.export_storage.redis.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/storages/export/redis", method="GET", params={"project": project}, request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[RedisExportStorage], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        project: typing.Optional[int] = OMIT,
        path: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        port: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        db: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RedisCreateResponse:
        """
        Create a new Redis export storage connection to store annotations.

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        path : typing.Optional[str]
            Storage prefix (optional)

        host : typing.Optional[str]
            Server Host IP (optional)

        port : typing.Optional[str]
            Server Port (optional)

        password : typing.Optional[str]
            Server Password (optional)

        db : typing.Optional[int]
            Database ID of database to use

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedisCreateResponse


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.export_storage.redis.create()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/storages/export/redis",
            method="POST",
            json={"project": project, "path": path, "host": host, "port": port, "password": password, "db": db},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RedisCreateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def validate(self, *, request_options: typing.Optional[RequestOptions] = None) -> RedisExportStorage:
        """
        Validate a specific Redis export storage connection.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedisExportStorage


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.export_storage.redis.validate()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/storages/export/redis/validate", method="POST", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RedisExportStorage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> RedisExportStorage:
        """
        Get a specific Redis export storage connection.

        Parameters
        ----------
        id : int
            A unique integer value identifying this redis export storage.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedisExportStorage


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.export_storage.redis.get(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/export/redis/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RedisExportStorage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a specific Redis export storage connection.

        Parameters
        ----------
        id : int
            A unique integer value identifying this redis export storage.

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
        await client.export_storage.redis.delete(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/export/redis/{jsonable_encoder(id)}", method="DELETE", request_options=request_options
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
        project: typing.Optional[int] = OMIT,
        path: typing.Optional[str] = OMIT,
        host: typing.Optional[str] = OMIT,
        port: typing.Optional[str] = OMIT,
        password: typing.Optional[str] = OMIT,
        db: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RedisUpdateResponse:
        """
        Update a specific Redis export storage connection.

        Parameters
        ----------
        id : int
            A unique integer value identifying this redis export storage.

        project : typing.Optional[int]
            Project ID

        path : typing.Optional[str]
            Storage prefix (optional)

        host : typing.Optional[str]
            Server Host IP (optional)

        port : typing.Optional[str]
            Server Port (optional)

        password : typing.Optional[str]
            Server Password (optional)

        db : typing.Optional[int]
            Database ID of database to use

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedisUpdateResponse


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.export_storage.redis.update(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/export/redis/{jsonable_encoder(id)}",
            method="PATCH",
            json={"project": project, "path": path, "host": host, "port": port, "password": password, "db": db},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RedisUpdateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def sync(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> RedisExportStorage:
        """
        Sync tasks from a specific Redis export storage connection.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RedisExportStorage


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.export_storage.redis.sync(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/export/redis/{jsonable_encoder(id)}/sync", method="POST", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(RedisExportStorage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
