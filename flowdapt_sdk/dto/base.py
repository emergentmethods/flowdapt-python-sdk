from typing import ClassVar

from flowdapt_sdk._compat import BaseModel


class BaseSchema(BaseModel):
    __version__: ClassVar[str] = "v1alpha1"
    __content_type__: ClassVar[str] = "application/json"
