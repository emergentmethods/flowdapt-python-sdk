from __future__ import annotations

from typing import Annotated

from flowdapt_sdk._compat import BaseModel, Field
from flowdapt_sdk.dto.base import BaseSchema


class V1Alpha1PluginMetadata(BaseModel):
    description: Annotated[str, Field(title='Description')]
    author: Annotated[str, Field(title='Author')]
    license: Annotated[str, Field(title='License')]
    url: Annotated[str, Field(title='Url')]
    version: Annotated[str, Field(title='Version', alias="version")]
    requirements: Annotated[list[str] | None, Field(title='Requirements')] = []


class V1Alpha1Plugin(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.plugin.v1alpha1+json"

    name: Annotated[str, Field(title='Name')]
    metadata: V1Alpha1PluginMetadata
    module: Annotated[str, Field(title='Module')]


class V1Alpha1PluginFiles(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.plugin_file.v1alpha1+json"

    files: Annotated[list[str], Field(title='Files')]
