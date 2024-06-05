# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.request_options import RequestOptions
from ...types.export import Export
from ...types.export_convert import ExportConvert
from ...types.export_create import ExportCreate

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ExportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_formats(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        Retrieve the available export formats for the current project by ID.

        Parameters
        ----------
        id : int
            A unique integer value identifying this project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Export formats

        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.projects.exports.list_formats(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/projects/{jsonable_encoder(id)}/export/formats", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[str], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Export]:
        """
        Returns a list of exported files for a specific project by ID.

        Parameters
        ----------
        id : int
            A unique integer value identifying this project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Export]


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.projects.exports.list(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/projects/{jsonable_encoder(id)}/exports/", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[Export], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self, id: int, *, request: ExportCreate, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportCreate:
        """
        Create a new export request to start a background task and generate an export file for a specific project by ID.

        Parameters
        ----------
        id : int
            A unique integer value identifying this project.

        request : ExportCreate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportCreate


        Examples
        --------
        from label_studio_sdk import ExportCreate
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.projects.exports.create(
            id=1,
            request=ExportCreate(),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/projects/{jsonable_encoder(id)}/exports/",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ExportCreate, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: int, export_pk: str, *, request_options: typing.Optional[RequestOptions] = None) -> Export:
        """
        Retrieve information about an export file by export ID for a specific project.

        Parameters
        ----------
        id : int
            A unique integer value identifying this project.

        export_pk : str
            Primary key identifying the export file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Export


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.projects.exports.get(
            id=1,
            export_pk="export_pk",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/projects/{jsonable_encoder(id)}/exports/{jsonable_encoder(export_pk)}",
            method="GET",
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Export, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: int, export_pk: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete an export file by specified export ID.

        Parameters
        ----------
        id : int
            A unique integer value identifying this project.

        export_pk : str
            Primary key identifying the export file.

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
        client.projects.exports.delete(
            id=1,
            export_pk="export_pk",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/projects/{jsonable_encoder(id)}/exports/{jsonable_encoder(export_pk)}",
            method="DELETE",
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def convert(
        self,
        id: int,
        export_pk: str,
        *,
        request: ExportConvert,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportConvert:
        """
        Convert export snapshot to selected format

        Parameters
        ----------
        id : int
            A unique integer value identifying this project.

        export_pk : str
            Primary key identifying the export file.

        request : ExportConvert

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportConvert


        Examples
        --------
        from label_studio_sdk import ExportConvert
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.projects.exports.convert(
            id=1,
            export_pk="export_pk",
            request=ExportConvert(
                export_type="export_type",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/projects/{jsonable_encoder(id)}/exports/{jsonable_encoder(export_pk)}/convert",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ExportConvert, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def download(
        self,
        id: int,
        export_pk: str,
        *,
        export_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Download an export file in the specified format for a specific project. Specify the project ID with the `id`
        parameter in the path and the ID of the export file you want to download using the `export_pk` parameter
        in the path.

        Get the `export_pk` from the response of the request to [Create new export](/api#operation/api_projects_exports_create)
        or after [listing export files](/api#operation/api_projects_exports_list).

        Parameters
        ----------
        id : int
            A unique integer value identifying this project.

        export_pk : str
            Primary key identifying the export file.

        export_type : typing.Optional[str]
            Selected export format

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
        client.projects.exports.download(
            id=1,
            export_pk="export_pk",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/projects/{jsonable_encoder(id)}/exports/{jsonable_encoder(export_pk)}/download",
            method="GET",
            params={"exportType": export_type},
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncExportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_formats(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Retrieve the available export formats for the current project by ID.

        Parameters
        ----------
        id : int
            A unique integer value identifying this project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Export formats

        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.projects.exports.list_formats(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/projects/{jsonable_encoder(id)}/export/formats", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[str], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Export]:
        """
        Returns a list of exported files for a specific project by ID.

        Parameters
        ----------
        id : int
            A unique integer value identifying this project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Export]


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.projects.exports.list(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/projects/{jsonable_encoder(id)}/exports/", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[Export], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self, id: int, *, request: ExportCreate, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportCreate:
        """
        Create a new export request to start a background task and generate an export file for a specific project by ID.

        Parameters
        ----------
        id : int
            A unique integer value identifying this project.

        request : ExportCreate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportCreate


        Examples
        --------
        from label_studio_sdk import ExportCreate
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.projects.exports.create(
            id=1,
            request=ExportCreate(),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/projects/{jsonable_encoder(id)}/exports/",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ExportCreate, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: int, export_pk: str, *, request_options: typing.Optional[RequestOptions] = None) -> Export:
        """
        Retrieve information about an export file by export ID for a specific project.

        Parameters
        ----------
        id : int
            A unique integer value identifying this project.

        export_pk : str
            Primary key identifying the export file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Export


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.projects.exports.get(
            id=1,
            export_pk="export_pk",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/projects/{jsonable_encoder(id)}/exports/{jsonable_encoder(export_pk)}",
            method="GET",
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Export, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: int, export_pk: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete an export file by specified export ID.

        Parameters
        ----------
        id : int
            A unique integer value identifying this project.

        export_pk : str
            Primary key identifying the export file.

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
        await client.projects.exports.delete(
            id=1,
            export_pk="export_pk",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/projects/{jsonable_encoder(id)}/exports/{jsonable_encoder(export_pk)}",
            method="DELETE",
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def convert(
        self,
        id: int,
        export_pk: str,
        *,
        request: ExportConvert,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ExportConvert:
        """
        Convert export snapshot to selected format

        Parameters
        ----------
        id : int
            A unique integer value identifying this project.

        export_pk : str
            Primary key identifying the export file.

        request : ExportConvert

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportConvert


        Examples
        --------
        from label_studio_sdk import ExportConvert
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.projects.exports.convert(
            id=1,
            export_pk="export_pk",
            request=ExportConvert(
                export_type="export_type",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/projects/{jsonable_encoder(id)}/exports/{jsonable_encoder(export_pk)}/convert",
            method="POST",
            json=request,
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(ExportConvert, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def download(
        self,
        id: int,
        export_pk: str,
        *,
        export_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Download an export file in the specified format for a specific project. Specify the project ID with the `id`
        parameter in the path and the ID of the export file you want to download using the `export_pk` parameter
        in the path.

        Get the `export_pk` from the response of the request to [Create new export](/api#operation/api_projects_exports_create)
        or after [listing export files](/api#operation/api_projects_exports_list).

        Parameters
        ----------
        id : int
            A unique integer value identifying this project.

        export_pk : str
            Primary key identifying the export file.

        export_type : typing.Optional[str]
            Selected export format

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
        await client.projects.exports.download(
            id=1,
            export_pk="export_pk",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/projects/{jsonable_encoder(id)}/exports/{jsonable_encoder(export_pk)}/download",
            method="GET",
            params={"exportType": export_type},
            request_options=request_options,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
