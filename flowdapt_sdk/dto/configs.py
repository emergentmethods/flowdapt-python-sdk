from __future__ import annotations

from enum import Enum
from typing import Any, Annotated

from flowdapt_sdk._compat import BaseModel, Field
from flowdapt_sdk.dto.base import BaseSchema
from flowdapt_sdk.dto.resource import V1Alpha1ResourceMetadata


class V1Alpha1ConfigSelectorType(Enum):
    name = 'name'
    annotation = 'annotation'


class V1Alpha2ConfigSelector(BaseModel):
    kind: Annotated[str | None, Field(title='Kind')] = None
    type: V1Alpha1ConfigSelectorType | None = 'name'
    value: Annotated[str | dict[str, str] | None, Field(title='Value')] = None


class V1Alpha1ConfigSelector(BaseModel):
    kind: Annotated[str | None, Field(title='Kind')] = None
    type: V1Alpha1ConfigSelectorType | None = 'name'
    value: Annotated[str | dict[str, str] | None, Field(title='Value')] = None


class V1Alpha1ConfigResourceSpec(BaseModel):
    selector: V1Alpha1ConfigSelector | None = None
    data: Annotated[dict[str, Any], Field(title='Data')]


class V1Alpha2ConfigResourceSpec(BaseModel):
    selector: V1Alpha2ConfigSelector | None = None
    data: Annotated[dict[str, Any], Field(title='Data')]
    new: Annotated[bool | None, Field(title='New')]


class V1Alpha1ConfigResourceCreateRequest(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.ai.config.v1alpha1+json"

    kind: Annotated[str, Field(title='Kind')]
    metadata: V1Alpha1ResourceMetadata
    spec: V1Alpha1ConfigResourceSpec


class V1Alpha1ConfigResourceCreateResponse(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.ai.config.v1alpha1+json"

    kind: Annotated[str, Field(title='Kind')]
    metadata: V1Alpha1ResourceMetadata
    spec: V1Alpha1ConfigResourceSpec


class V1Alpha2ConfigResourceCreateRequest(BaseSchema):
    __version__ = "v1alpha2"
    __content_type__ = "application/vnd.flowdapt.ai.config.v1alpha2+json"

    kind: Annotated[str, Field(title='Kind')]
    metadata: V1Alpha1ResourceMetadata
    spec: V1Alpha2ConfigResourceSpec


class V1Alpha2ConfigResourceCreateResponse(BaseSchema):
    __version__ = "v1alpha2"
    __content_type__ = "application/vnd.flowdapt.ai.config.v1alpha2+json"

    kind: Annotated[str, Field(title='Kind')] = "config"
    metadata: V1Alpha1ResourceMetadata
    spec: V1Alpha2ConfigResourceSpec


class V1Alpha1ConfigResourceUpdateRequest(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.ai.config.v1alpha1+json"

    kind: Annotated[str, Field(title='Kind')] = "config"
    metadata: V1Alpha1ResourceMetadata
    spec: V1Alpha1ConfigResourceSpec


class V1Alpha1ConfigResourceUpdateResponse(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.ai.config.v1alpha1+json"

    kind: Annotated[str, Field(title='Kind')] = "config"
    metadata: V1Alpha1ResourceMetadata
    spec: V1Alpha1ConfigResourceSpec


class V1Alpha1ConfigResourceReadResponse(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.ai.config.v1alpha1+json"

    kind: Annotated[str, Field(title='Kind')] = "config"
    metadata: V1Alpha1ResourceMetadata
    spec: V1Alpha1ConfigResourceSpec
