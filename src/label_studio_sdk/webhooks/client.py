# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.query_encoder import encode_query
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..types.webhook import Webhook
from ..types.webhook_serializer_for_update import WebhookSerializerForUpdate
from .types.webhooks_update_request_actions_item import WebhooksUpdateRequestActionsItem

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class WebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, project: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Webhook]:
        """
        List all webhooks set up for your organization.

        Parameters
        ----------
        project : typing.Optional[str]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Webhook]


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/webhooks/"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "project": project,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[Webhook], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(self, *, request: Webhook, request_options: typing.Optional[RequestOptions] = None) -> Webhook:
        """
        Create a webhook for your organization.

        Parameters
        ----------
        request : Webhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook


        Examples
        --------
        from label_studio_sdk import Webhook
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.create(
            request=Webhook(
                url="url",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/webhooks/"),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Webhook, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def info(
        self,
        *,
        organization_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get descriptions of all available webhook actions to set up webhooks.

        Parameters
        ----------
        organization_only : typing.Optional[bool]
            organization-only or not

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
        client.webhooks.info()
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/webhooks/info/"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "organization-only": organization_only,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Webhook:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook


        Examples
        --------
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.get(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/webhooks/{jsonable_encoder(id)}/"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Webhook, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this webhook.

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
        client.webhooks.delete(
            id=1,
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/webhooks/{jsonable_encoder(id)}/"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
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
        url: str,
        request: WebhookSerializerForUpdate,
        send_payload: typing.Optional[bool] = None,
        send_for_all_actions: typing.Optional[bool] = None,
        headers: typing.Optional[str] = None,
        is_active: typing.Optional[bool] = None,
        actions: typing.Optional[
            typing.Union[WebhooksUpdateRequestActionsItem, typing.Sequence[WebhooksUpdateRequestActionsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookSerializerForUpdate:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this webhook.

        url : str
            URL of webhook

        request : WebhookSerializerForUpdate

        send_payload : typing.Optional[bool]
            If value is False send only action

        send_for_all_actions : typing.Optional[bool]
            If value is False - used only for actions from WebhookAction

        headers : typing.Optional[str]
            Key Value Json of headers

        is_active : typing.Optional[bool]
            If value is False the webhook is disabled

        actions : typing.Optional[typing.Union[WebhooksUpdateRequestActionsItem, typing.Sequence[WebhooksUpdateRequestActionsItem]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookSerializerForUpdate


        Examples
        --------
        from label_studio_sdk import WebhookSerializerForUpdate
        from label_studio_sdk.client import LabelStudio

        client = LabelStudio(
            api_key="YOUR_API_KEY",
        )
        client.webhooks.update(
            id=1,
            url="url",
            request=WebhookSerializerForUpdate(
                url="url",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="PATCH",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/webhooks/{jsonable_encoder(id)}/"
            ),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "url": url,
                            "send_payload": send_payload,
                            "send_for_all_actions": send_for_all_actions,
                            "headers": headers,
                            "is_active": is_active,
                            "actions": actions,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(WebhookSerializerForUpdate, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, project: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Webhook]:
        """
        List all webhooks set up for your organization.

        Parameters
        ----------
        project : typing.Optional[str]
            Project ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Webhook]


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.webhooks.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/webhooks/"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "project": project,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(typing.List[Webhook], _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(self, *, request: Webhook, request_options: typing.Optional[RequestOptions] = None) -> Webhook:
        """
        Create a webhook for your organization.

        Parameters
        ----------
        request : Webhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook


        Examples
        --------
        from label_studio_sdk import Webhook
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.webhooks.create(
            request=Webhook(
                url="url",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="POST",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/webhooks/"),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Webhook, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def info(
        self,
        *,
        organization_only: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get descriptions of all available webhook actions to set up webhooks.

        Parameters
        ----------
        organization_only : typing.Optional[bool]
            organization-only or not

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
        await client.webhooks.info()
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "api/webhooks/info/"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "organization-only": organization_only,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> Webhook:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Webhook


        Examples
        --------
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.webhooks.get(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/webhooks/{jsonable_encoder(id)}/"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(Webhook, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this webhook.

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
        await client.webhooks.delete(
            id=1,
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/webhooks/{jsonable_encoder(id)}/"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
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
        url: str,
        request: WebhookSerializerForUpdate,
        send_payload: typing.Optional[bool] = None,
        send_for_all_actions: typing.Optional[bool] = None,
        headers: typing.Optional[str] = None,
        is_active: typing.Optional[bool] = None,
        actions: typing.Optional[
            typing.Union[WebhooksUpdateRequestActionsItem, typing.Sequence[WebhooksUpdateRequestActionsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookSerializerForUpdate:
        """


        Parameters
        ----------
        id : int
            A unique integer value identifying this webhook.

        url : str
            URL of webhook

        request : WebhookSerializerForUpdate

        send_payload : typing.Optional[bool]
            If value is False send only action

        send_for_all_actions : typing.Optional[bool]
            If value is False - used only for actions from WebhookAction

        headers : typing.Optional[str]
            Key Value Json of headers

        is_active : typing.Optional[bool]
            If value is False the webhook is disabled

        actions : typing.Optional[typing.Union[WebhooksUpdateRequestActionsItem, typing.Sequence[WebhooksUpdateRequestActionsItem]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookSerializerForUpdate


        Examples
        --------
        from label_studio_sdk import WebhookSerializerForUpdate
        from label_studio_sdk.client import AsyncLabelStudio

        client = AsyncLabelStudio(
            api_key="YOUR_API_KEY",
        )
        await client.webhooks.update(
            id=1,
            url="url",
            request=WebhookSerializerForUpdate(
                url="url",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="PATCH",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"api/webhooks/{jsonable_encoder(id)}/"
            ),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "url": url,
                            "send_payload": send_payload,
                            "send_for_all_actions": send_for_all_actions,
                            "headers": headers,
                            "is_active": is_active,
                            "actions": actions,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return pydantic_v1.parse_obj_as(WebhookSerializerForUpdate, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
