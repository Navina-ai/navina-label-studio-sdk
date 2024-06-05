# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.request_options import RequestOptions
from ...types.azure_blob_import_storage import AzureBlobImportStorage
from .types.azure_create_response import AzureCreateResponse
from .types.azure_update_response import AzureUpdateResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AzureClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, project: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AzureBlobImportStorage]:
        """
        Get list of all Azure import storage connections.

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AzureBlobImportStorage]


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.import_storage.azure.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/storages/azure/", method="GET", params={"project": project}, request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[AzureBlobImportStorage], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        project: typing.Optional[int] = OMIT,
        container: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        regex_filter: typing.Optional[str] = OMIT,
        use_blob_urls: typing.Optional[bool] = OMIT,
        account_name: typing.Optional[str] = OMIT,
        account_key: typing.Optional[str] = OMIT,
        presign: typing.Optional[bool] = OMIT,
        presign_ttl: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AzureCreateResponse:
        """
        Get new Azure import storage

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        container : typing.Optional[str]
            Azure blob container

        prefix : typing.Optional[str]
            Azure blob prefix name

        regex_filter : typing.Optional[str]
            Cloud storage regex for filtering objects

        use_blob_urls : typing.Optional[bool]
            Interpret objects as BLOBs and generate URLs

        account_name : typing.Optional[str]
            Azure Blob account name

        account_key : typing.Optional[str]
            Azure Blob account key

        presign : typing.Optional[bool]
            Presign URLs for direct download

        presign_ttl : typing.Optional[int]
            Presign TTL in minutes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AzureCreateResponse


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.import_storage.azure.create()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/storages/azure/",
            method="POST",
            json={
                "project": project,
                "container": container,
                "prefix": prefix,
                "regex_filter": regex_filter,
                "use_blob_urls": use_blob_urls,
                "account_name": account_name,
                "account_key": account_key,
                "presign": presign,
                "presign_ttl": presign_ttl,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(AzureCreateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def validate(self, *, request_options: typing.Optional[RequestOptions] = None) -> AzureBlobImportStorage:
        """
        Validate a specific Azure import storage connection.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AzureBlobImportStorage


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.import_storage.azure.validate()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/storages/azure/validate", method="POST", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(AzureBlobImportStorage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> AzureBlobImportStorage:
        """
        Get a specific Azure import storage connection.

        Parameters
        ----------
        id : int
            A unique integer value identifying this azure blob import storage.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AzureBlobImportStorage


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.import_storage.azure.get(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/azure/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(AzureBlobImportStorage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a specific Azure import storage connection.

        Parameters
        ----------
        id : int
            A unique integer value identifying this azure blob import storage.

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
        client.import_storage.azure.delete(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/azure/{jsonable_encoder(id)}", method="DELETE", request_options=request_options
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
        container: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        regex_filter: typing.Optional[str] = OMIT,
        use_blob_urls: typing.Optional[bool] = OMIT,
        account_name: typing.Optional[str] = OMIT,
        account_key: typing.Optional[str] = OMIT,
        presign: typing.Optional[bool] = OMIT,
        presign_ttl: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AzureUpdateResponse:
        """
        Update a specific Azure import storage connection.

        Parameters
        ----------
        id : int
            A unique integer value identifying this azure blob import storage.

        project : typing.Optional[int]
            Project ID

        container : typing.Optional[str]
            Azure blob container

        prefix : typing.Optional[str]
            Azure blob prefix name

        regex_filter : typing.Optional[str]
            Cloud storage regex for filtering objects

        use_blob_urls : typing.Optional[bool]
            Interpret objects as BLOBs and generate URLs

        account_name : typing.Optional[str]
            Azure Blob account name

        account_key : typing.Optional[str]
            Azure Blob account key

        presign : typing.Optional[bool]
            Presign URLs for direct download

        presign_ttl : typing.Optional[int]
            Presign TTL in minutes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AzureUpdateResponse


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.import_storage.azure.update(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/azure/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "project": project,
                "container": container,
                "prefix": prefix,
                "regex_filter": regex_filter,
                "use_blob_urls": use_blob_urls,
                "account_name": account_name,
                "account_key": account_key,
                "presign": presign,
                "presign_ttl": presign_ttl,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(AzureUpdateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def sync(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> AzureBlobImportStorage:
        """
        Sync tasks from an Azure import storage connection.

        Parameters
        ----------
        id : int
            Storage ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AzureBlobImportStorage


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.import_storage.azure.sync(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/storages/azure/{jsonable_encoder(id)}/sync", method="POST", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(AzureBlobImportStorage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAzureClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, project: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AzureBlobImportStorage]:
        """
        Get list of all Azure import storage connections.

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AzureBlobImportStorage]


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.import_storage.azure.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/storages/azure/", method="GET", params={"project": project}, request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[AzureBlobImportStorage], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        project: typing.Optional[int] = OMIT,
        container: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        regex_filter: typing.Optional[str] = OMIT,
        use_blob_urls: typing.Optional[bool] = OMIT,
        account_name: typing.Optional[str] = OMIT,
        account_key: typing.Optional[str] = OMIT,
        presign: typing.Optional[bool] = OMIT,
        presign_ttl: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AzureCreateResponse:
        """
        Get new Azure import storage

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        container : typing.Optional[str]
            Azure blob container

        prefix : typing.Optional[str]
            Azure blob prefix name

        regex_filter : typing.Optional[str]
            Cloud storage regex for filtering objects

        use_blob_urls : typing.Optional[bool]
            Interpret objects as BLOBs and generate URLs

        account_name : typing.Optional[str]
            Azure Blob account name

        account_key : typing.Optional[str]
            Azure Blob account key

        presign : typing.Optional[bool]
            Presign URLs for direct download

        presign_ttl : typing.Optional[int]
            Presign TTL in minutes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AzureCreateResponse


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.import_storage.azure.create()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/storages/azure/",
            method="POST",
            json={
                "project": project,
                "container": container,
                "prefix": prefix,
                "regex_filter": regex_filter,
                "use_blob_urls": use_blob_urls,
                "account_name": account_name,
                "account_key": account_key,
                "presign": presign,
                "presign_ttl": presign_ttl,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(AzureCreateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def validate(self, *, request_options: typing.Optional[RequestOptions] = None) -> AzureBlobImportStorage:
        """
        Validate a specific Azure import storage connection.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AzureBlobImportStorage


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.import_storage.azure.validate()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/storages/azure/validate", method="POST", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(AzureBlobImportStorage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> AzureBlobImportStorage:
        """
        Get a specific Azure import storage connection.

        Parameters
        ----------
        id : int
            A unique integer value identifying this azure blob import storage.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AzureBlobImportStorage


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.import_storage.azure.get(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/azure/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(AzureBlobImportStorage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a specific Azure import storage connection.

        Parameters
        ----------
        id : int
            A unique integer value identifying this azure blob import storage.

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
        await client.import_storage.azure.delete(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/azure/{jsonable_encoder(id)}", method="DELETE", request_options=request_options
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
        container: typing.Optional[str] = OMIT,
        prefix: typing.Optional[str] = OMIT,
        regex_filter: typing.Optional[str] = OMIT,
        use_blob_urls: typing.Optional[bool] = OMIT,
        account_name: typing.Optional[str] = OMIT,
        account_key: typing.Optional[str] = OMIT,
        presign: typing.Optional[bool] = OMIT,
        presign_ttl: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AzureUpdateResponse:
        """
        Update a specific Azure import storage connection.

        Parameters
        ----------
        id : int
            A unique integer value identifying this azure blob import storage.

        project : typing.Optional[int]
            Project ID

        container : typing.Optional[str]
            Azure blob container

        prefix : typing.Optional[str]
            Azure blob prefix name

        regex_filter : typing.Optional[str]
            Cloud storage regex for filtering objects

        use_blob_urls : typing.Optional[bool]
            Interpret objects as BLOBs and generate URLs

        account_name : typing.Optional[str]
            Azure Blob account name

        account_key : typing.Optional[str]
            Azure Blob account key

        presign : typing.Optional[bool]
            Presign URLs for direct download

        presign_ttl : typing.Optional[int]
            Presign TTL in minutes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AzureUpdateResponse


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.import_storage.azure.update(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/azure/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "project": project,
                "container": container,
                "prefix": prefix,
                "regex_filter": regex_filter,
                "use_blob_urls": use_blob_urls,
                "account_name": account_name,
                "account_key": account_key,
                "presign": presign,
                "presign_ttl": presign_ttl,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(AzureUpdateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def sync(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> AzureBlobImportStorage:
        """
        Sync tasks from an Azure import storage connection.

        Parameters
        ----------
        id : int
            Storage ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AzureBlobImportStorage


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.import_storage.azure.sync(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/storages/azure/{jsonable_encoder(id)}/sync", method="POST", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(AzureBlobImportStorage, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
