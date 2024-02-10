from __future__ import annotations

from enum import Enum
from typing import Any, Annotated

from flowdapt_sdk._compat import BaseModel, Field
from flowdapt_sdk.dto.base import BaseSchema
from flowdapt_sdk.dto.resource import V1Alpha1ResourceMetadata


class V1Alpha1TriggerRuleType(Enum):
    schedule = 'schedule'
    condition = 'condition'


class V1Alpha1TriggerRuleAction(BaseModel):
    target: Annotated[str, Field(title='Target')]
    parameters: Annotated[dict[str, Any] | None, Field(title='Parameters')] = {}


class V1Alpha1TriggerRuleResourceSpec(BaseModel):
    type: V1Alpha1TriggerRuleType | None = 'condition'
    rule: Annotated[dict[str, Any] | list[str], Field(title='Rule')]
    action: V1Alpha1TriggerRuleAction


class V1Alpha1TriggerRuleResourceCreateRequest(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.trigger_rule.v1alpha1+json"

    kind: Annotated[str | None, Field(title='Kind')] = "trigger_rule"
    metadata: V1Alpha1ResourceMetadata
    spec: V1Alpha1TriggerRuleResourceSpec


class V1Alpha1TriggerRuleResourceCreateResponse(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.trigger_rule.v1alpha1+json"

    kind: Annotated[str | None, Field(title='Kind')] = "trigger_rule"
    metadata: V1Alpha1ResourceMetadata
    spec: V1Alpha1TriggerRuleResourceSpec


class V1Alpha1TriggerRuleResourceUpdateRequest(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.trigger_rule.v1alpha1+json"

    kind: Annotated[str | None, Field(title='Kind')] = "trigger_rule"
    metadata: V1Alpha1ResourceMetadata
    spec: V1Alpha1TriggerRuleResourceSpec


class V1Alpha1TriggerRuleResourceUpdateResponse(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.trigger_rule.v1alpha1+json"

    kind: Annotated[str | None, Field(title='Kind')] = "trigger_rule"
    metadata: V1Alpha1ResourceMetadata
    spec: V1Alpha1TriggerRuleResourceSpec


class V1Alpha1TriggerRuleResourceReadResponse(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.trigger_rule.v1alpha1+json"

    kind: Annotated[str | None, Field(title='Kind')] = "trigger_rule"
    metadata: V1Alpha1ResourceMetadata
    spec: V1Alpha1TriggerRuleResourceSpec
