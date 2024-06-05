# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..types.ml_backend import MlBackend
from .types.ml_create_request_auth_method import MlCreateRequestAuthMethod
from .types.ml_create_response import MlCreateResponse
from .types.ml_update_request_auth_method import MlUpdateRequestAuthMethod
from .types.ml_update_response import MlUpdateResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class MlClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, project: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MlBackend]:
        """
        List all configured ML backends for a specific project by ID.
        Use the following cURL command:

        ```bash
        curl https://localhost:8080/api/ml?project={project_id} -H 'Authorization: Token abc123'
        ```

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MlBackend]


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.ml.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/ml/", method="GET", params={"project": project}, request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[MlBackend], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        url: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        is_interactive: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        auth_method: typing.Optional[MlCreateRequestAuthMethod] = OMIT,
        basic_auth_user: typing.Optional[str] = OMIT,
        basic_auth_pass: typing.Optional[str] = OMIT,
        extra_params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MlCreateResponse:
        """
        Add an ML backend to a project using the Label Studio UI or by sending a POST request using the following cURL
        command:
        
        ```bash
        curl -X POST -H 'Content-type: application/json' https://localhost:8080/api/ml -H 'Authorization: Token abc123'\
        --data '{"url": "http://localhost:9090", "project": {project_id}}'
        ```
        
        Parameters
        ----------
        url : typing.Optional[str]
            ML backend URL
        
        project : typing.Optional[int]
            Project ID
        
        is_interactive : typing.Optional[bool]
            Is interactive
        
        title : typing.Optional[str]
            Title
        
        description : typing.Optional[str]
            Description
        
        auth_method : typing.Optional[MlCreateRequestAuthMethod]
            Auth method
        
        basic_auth_user : typing.Optional[str]
            Basic auth user
        
        basic_auth_pass : typing.Optional[str]
            Basic auth password
        
        extra_params : typing.Optional[typing.Dict[str, typing.Any]]
            Extra parameters
        
        timeout : typing.Optional[int]
            Response model timeout
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        MlCreateResponse
            
        
        Examples
        --------
        from label_studio_sdk.client import LabelStudio
        
        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.ml.create()
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/ml/",
            method="POST",
            json={
                "url": url,
                "project": project,
                "is_interactive": is_interactive,
                "title": title,
                "description": description,
                "auth_method": auth_method,
                "basic_auth_user": basic_auth_user,
                "basic_auth_pass": basic_auth_pass,
                "extra_params": extra_params,
                "timeout": timeout,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(MlCreateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> MlBackend:
        """
        Get details about a specific ML backend connection by ID. For example, make a GET request using the
        following cURL command:

        ```bash
        curl https://localhost:8080/api/ml/{ml_backend_ID} -H 'Authorization: Token abc123'
        ```

        Parameters
        ----------
        id : int
            A unique integer value identifying this ml backend.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MlBackend


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.ml.get(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(MlBackend, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Remove an existing ML backend connection by ID. For example, use the
        following cURL command:

        ```bash
        curl -X DELETE https://localhost:8080/api/ml/{ml_backend_ID} -H 'Authorization: Token abc123'
        ```

        Parameters
        ----------
        id : int
            A unique integer value identifying this ml backend.

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
        client.ml.delete(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}", method="DELETE", request_options=request_options
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
        url: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        is_interactive: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        auth_method: typing.Optional[MlUpdateRequestAuthMethod] = OMIT,
        basic_auth_user: typing.Optional[str] = OMIT,
        basic_auth_pass: typing.Optional[str] = OMIT,
        extra_params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MlUpdateResponse:
        """
        Update ML backend parameters using the Label Studio UI or by sending a PATCH request using the following cURL command:
        
        ```bash
        curl -X PATCH -H 'Content-type: application/json' https://localhost:8080/api/ml/{ml_backend_ID} -H 'Authorization: Token abc123'\
        --data '{"url": "http://localhost:9091"}'
        ```
        
        Parameters
        ----------
        id : int
            A unique integer value identifying this ml backend.
        
        url : typing.Optional[str]
            ML backend URL
        
        project : typing.Optional[int]
            Project ID
        
        is_interactive : typing.Optional[bool]
            Is interactive
        
        title : typing.Optional[str]
            Title
        
        description : typing.Optional[str]
            Description
        
        auth_method : typing.Optional[MlUpdateRequestAuthMethod]
            Auth method
        
        basic_auth_user : typing.Optional[str]
            Basic auth user
        
        basic_auth_pass : typing.Optional[str]
            Basic auth password
        
        extra_params : typing.Optional[typing.Dict[str, typing.Any]]
            Extra parameters
        
        timeout : typing.Optional[int]
            Response model timeout
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        MlUpdateResponse
            
        
        Examples
        --------
        from label_studio_sdk.client import LabelStudio
        
        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.ml.update(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "url": url,
                "project": project,
                "is_interactive": is_interactive,
                "title": title,
                "description": description,
                "auth_method": auth_method,
                "basic_auth_user": basic_auth_user,
                "basic_auth_pass": basic_auth_pass,
                "extra_params": extra_params,
                "timeout": timeout,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(MlUpdateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def predict_interactive(
        self,
        id: int,
        *,
        task: int,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Send a request to the machine learning backend set up to be used for interactive preannotations to retrieve a
        predicted region based on annotator input.
        See [set up machine learning](https://labelstud.io/guide/ml.html#Get-interactive-preannotations) for more.

        Parameters
        ----------
        id : int
            A unique integer value identifying this ML backend.

        task : int
            ID of task to annotate

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Context for ML model

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
        client.ml.predict_interactive(
            id=1,
            task=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}/interactive-annotating",
            method="POST",
            json={"task": task, "context": context},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def train(
        self,
        id: int,
        *,
        use_ground_truth: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        After you add an ML backend, call this API with the ML backend ID to start training with
        already-labeled tasks.

        Get the ML backend ID by [listing the ML backends for a project](https://labelstud.io/api/#operation/api_ml_list).

        Parameters
        ----------
        id : int
            A unique integer value identifying this ML backend.

        use_ground_truth : typing.Optional[bool]
            Whether to include ground truth annotations in training

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
        client.ml.train(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}/train",
            method="POST",
            json={"use_ground_truth": use_ground_truth},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 500:
            raise InternalServerError(pydantic_v1.parse_obj_as(str, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_model_versions(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get available versions of the model.

        Parameters
        ----------
        id : str

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
        client.ml.list_model_versions(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}/versions", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncMlClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, project: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[MlBackend]:
        """
        List all configured ML backends for a specific project by ID.
        Use the following cURL command:

        ```bash
        curl https://localhost:8080/api/ml?project={project_id} -H 'Authorization: Token abc123'
        ```

        Parameters
        ----------
        project : typing.Optional[int]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[MlBackend]


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.ml.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/ml/", method="GET", params={"project": project}, request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[MlBackend], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        url: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        is_interactive: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        auth_method: typing.Optional[MlCreateRequestAuthMethod] = OMIT,
        basic_auth_user: typing.Optional[str] = OMIT,
        basic_auth_pass: typing.Optional[str] = OMIT,
        extra_params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MlCreateResponse:
        """
        Add an ML backend to a project using the Label Studio UI or by sending a POST request using the following cURL
        command:
        
        ```bash
        curl -X POST -H 'Content-type: application/json' https://localhost:8080/api/ml -H 'Authorization: Token abc123'\
        --data '{"url": "http://localhost:9090", "project": {project_id}}'
        ```
        
        Parameters
        ----------
        url : typing.Optional[str]
            ML backend URL
        
        project : typing.Optional[int]
            Project ID
        
        is_interactive : typing.Optional[bool]
            Is interactive
        
        title : typing.Optional[str]
            Title
        
        description : typing.Optional[str]
            Description
        
        auth_method : typing.Optional[MlCreateRequestAuthMethod]
            Auth method
        
        basic_auth_user : typing.Optional[str]
            Basic auth user
        
        basic_auth_pass : typing.Optional[str]
            Basic auth password
        
        extra_params : typing.Optional[typing.Dict[str, typing.Any]]
            Extra parameters
        
        timeout : typing.Optional[int]
            Response model timeout
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        MlCreateResponse
            
        
        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio
        
        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.ml.create()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/ml/",
            method="POST",
            json={
                "url": url,
                "project": project,
                "is_interactive": is_interactive,
                "title": title,
                "description": description,
                "auth_method": auth_method,
                "basic_auth_user": basic_auth_user,
                "basic_auth_pass": basic_auth_pass,
                "extra_params": extra_params,
                "timeout": timeout,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(MlCreateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> MlBackend:
        """
        Get details about a specific ML backend connection by ID. For example, make a GET request using the
        following cURL command:

        ```bash
        curl https://localhost:8080/api/ml/{ml_backend_ID} -H 'Authorization: Token abc123'
        ```

        Parameters
        ----------
        id : int
            A unique integer value identifying this ml backend.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MlBackend


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.ml.get(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(MlBackend, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Remove an existing ML backend connection by ID. For example, use the
        following cURL command:

        ```bash
        curl -X DELETE https://localhost:8080/api/ml/{ml_backend_ID} -H 'Authorization: Token abc123'
        ```

        Parameters
        ----------
        id : int
            A unique integer value identifying this ml backend.

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
        await client.ml.delete(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}", method="DELETE", request_options=request_options
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
        url: typing.Optional[str] = OMIT,
        project: typing.Optional[int] = OMIT,
        is_interactive: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        auth_method: typing.Optional[MlUpdateRequestAuthMethod] = OMIT,
        basic_auth_user: typing.Optional[str] = OMIT,
        basic_auth_pass: typing.Optional[str] = OMIT,
        extra_params: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MlUpdateResponse:
        """
        Update ML backend parameters using the Label Studio UI or by sending a PATCH request using the following cURL command:
        
        ```bash
        curl -X PATCH -H 'Content-type: application/json' https://localhost:8080/api/ml/{ml_backend_ID} -H 'Authorization: Token abc123'\
        --data '{"url": "http://localhost:9091"}'
        ```
        
        Parameters
        ----------
        id : int
            A unique integer value identifying this ml backend.
        
        url : typing.Optional[str]
            ML backend URL
        
        project : typing.Optional[int]
            Project ID
        
        is_interactive : typing.Optional[bool]
            Is interactive
        
        title : typing.Optional[str]
            Title
        
        description : typing.Optional[str]
            Description
        
        auth_method : typing.Optional[MlUpdateRequestAuthMethod]
            Auth method
        
        basic_auth_user : typing.Optional[str]
            Basic auth user
        
        basic_auth_pass : typing.Optional[str]
            Basic auth password
        
        extra_params : typing.Optional[typing.Dict[str, typing.Any]]
            Extra parameters
        
        timeout : typing.Optional[int]
            Response model timeout
        
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.
        
        Returns
        -------
        MlUpdateResponse
            
        
        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio
        
        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.ml.update(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "url": url,
                "project": project,
                "is_interactive": is_interactive,
                "title": title,
                "description": description,
                "auth_method": auth_method,
                "basic_auth_user": basic_auth_user,
                "basic_auth_pass": basic_auth_pass,
                "extra_params": extra_params,
                "timeout": timeout,
            },
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(MlUpdateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def predict_interactive(
        self,
        id: int,
        *,
        task: int,
        context: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Send a request to the machine learning backend set up to be used for interactive preannotations to retrieve a
        predicted region based on annotator input.
        See [set up machine learning](https://labelstud.io/guide/ml.html#Get-interactive-preannotations) for more.

        Parameters
        ----------
        id : int
            A unique integer value identifying this ML backend.

        task : int
            ID of task to annotate

        context : typing.Optional[typing.Dict[str, typing.Any]]
            Context for ML model

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
        await client.ml.predict_interactive(
            id=1,
            task=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}/interactive-annotating",
            method="POST",
            json={"task": task, "context": context},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def train(
        self,
        id: int,
        *,
        use_ground_truth: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        After you add an ML backend, call this API with the ML backend ID to start training with
        already-labeled tasks.

        Get the ML backend ID by [listing the ML backends for a project](https://labelstud.io/api/#operation/api_ml_list).

        Parameters
        ----------
        id : int
            A unique integer value identifying this ML backend.

        use_ground_truth : typing.Optional[bool]
            Whether to include ground truth annotations in training

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
        await client.ml.train(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}/train",
            method="POST",
            json={"use_ground_truth": use_ground_truth},
            request_options=request_options,
            omit=OMIT,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 500:
            raise InternalServerError(pydantic_v1.parse_obj_as(str, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_model_versions(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get available versions of the model.

        Parameters
        ----------
        id : str

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
        await client.ml.list_model_versions(
            id="id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/ml/{jsonable_encoder(id)}/versions", method="GET", request_options=request_options
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
