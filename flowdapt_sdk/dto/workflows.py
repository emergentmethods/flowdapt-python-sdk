from __future__ import annotations

from datetime import datetime
from uuid import UUID
from typing import Any, Annotated

from flowdapt_sdk._compat import BaseModel, Field
from flowdapt_sdk.dto.base import BaseSchema
from flowdapt_sdk.dto.resource import V1Alpha1ResourceMetadata


class V1Alpha1WorkflowStage(BaseModel):
    type: Annotated[str, Field(title='Type')] = "simple"
    target: Annotated[str, Field(title='Target')]
    name: Annotated[str, Field(title='Name')]
    description: Annotated[str, Field(title='Description')] = ""
    version: Annotated[str, Field(title='Version')] = ""
    depends_on: Annotated[list[str], Field(title='Depends On')] = []
    options: Annotated[dict[str, Any], Field(title='Options')] = {}
    resources: Annotated[dict[str, Any], Field(title='Resources')] = {}
    priority: Annotated[int | None, Field(title='Priority')] = None


class V1Alpha1WorkflowResourceSpec(BaseModel):
    stages: Annotated[list[V1Alpha1WorkflowStage], Field(title='Stages')]


class V1Alpha1WorkflowResourceCreateRequest(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.workflow.v1alpha1+json"

    kind: Annotated[str | None, Field(title='Kind')] = "workflow"
    metadata: V1Alpha1ResourceMetadata
    spec: V1Alpha1WorkflowResourceSpec


class V1Alpha1WorkflowResourceCreateResponse(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.workflow.v1alpha1+json"

    kind: Annotated[str | None, Field(title='Kind')] = "workflow"
    metadata: V1Alpha1ResourceMetadata
    spec: V1Alpha1WorkflowResourceSpec


class V1Alpha1WorkflowResourceUpdateResponse(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.workflow.v1alpha1+json"

    kind: Annotated[str | None, Field(title='Kind')] = "workflow"
    metadata: V1Alpha1ResourceMetadata
    spec: V1Alpha1WorkflowResourceSpec


class V1Alpha1WorkflowResourceUpdateRequest(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.workflow.v1alpha1+json"

    kind: Annotated[str | None, Field(title='Kind')] = "workflow"
    metadata: V1Alpha1ResourceMetadata
    spec: V1Alpha1WorkflowResourceSpec


class V1Alpha1WorkflowResourceReadResponse(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.workflow.v1alpha1+json"

    kind: Annotated[str | None, Field(title='Kind')] = "workflow"
    metadata: V1Alpha1ResourceMetadata
    spec: V1Alpha1WorkflowResourceSpec


class V1Alpha1WorkflowRunReadResponse(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.workflow_run.v1alpha1+json"

    uid: Annotated[UUID, Field(title='Uid')]
    name: Annotated[str, Field(title='Name')]
    workflow: Annotated[str, Field(title='Workflow')]
    started_at: Annotated[datetime, Field(title='Started At')]
    finished_at: Annotated[datetime | None, Field(title='Finished At')] = None
    result: Annotated[Any | None, Field(title='Result')] = None
    state: Annotated[str, Field(title='State')]
