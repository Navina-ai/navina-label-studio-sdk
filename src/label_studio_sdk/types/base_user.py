# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import datetime as dt
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BaseUser(UniversalBaseModel):
    id: typing.Optional[int] = None
    first_name: typing.Optional[str] = None
    last_name: typing.Optional[str] = None
    username: str
    email: typing.Optional[str] = None
    last_activity: typing.Optional[dt.datetime] = None
    avatar: typing.Optional[str] = None
    initials: typing.Optional[str] = None
    phone: typing.Optional[str] = None
    active_organization: typing.Optional[int] = None
    allow_newsletters: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Allow sending newsletters to user
    """

    date_joined: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
