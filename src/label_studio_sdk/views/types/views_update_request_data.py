# This file was auto-generated by Fern from our API Definition.

from ...core.pydantic_utilities import UniversalBaseModel
import typing
from .views_update_request_data_filters import ViewsUpdateRequestDataFilters
import pydantic
from .views_update_request_data_ordering_item import ViewsUpdateRequestDataOrderingItem
from ...core.pydantic_utilities import IS_PYDANTIC_V2


class ViewsUpdateRequestData(UniversalBaseModel):
    """
    Custom view data
    """

    filters: typing.Optional[ViewsUpdateRequestDataFilters] = pydantic.Field(default=None)
    """
    Filters to apply on tasks. You can use [the helper class `Filters` from this page](https://labelstud.io/sdk/data_manager.html) to create Data Manager Filters.<br>Example: `{"conjunction": "or", "items": [{"filter": "filter:tasks:completed_at", "operator": "greater", "type": "Datetime", "value": "2021-01-01T00:00:00.000Z"}]}`
    """

    ordering: typing.Optional[typing.List[ViewsUpdateRequestDataOrderingItem]] = pydantic.Field(default=None)
    """
    List of fields to order by. Fields are similar to filters but without the `filter:` prefix. To reverse the order, add a minus sign before the field name, e.g. `-tasks:created_at`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
