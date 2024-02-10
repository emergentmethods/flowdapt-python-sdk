from __future__ import annotations

from typing import Any, Annotated

from flowdapt_sdk._compat import BaseModel, RootModel, Field
from flowdapt_sdk.dto.base import BaseSchema


class V1Alpha1MetricsBucketValue(BaseModel):
    attributes: Annotated[dict[str, Any], Field(title='Attributes')]
    start_time_unix_nano: Annotated[int, Field(title='Start Time Unix Nano')]
    time_unix_nano: Annotated[int, Field(title='Time Unix Nano')]
    count: Annotated[int, Field(title='Count')]
    bucket_counts: Annotated[list[int], Field(title='Bucket Counts')]
    explicit_bounds: Annotated[list[float | int], Field(title='Explicit Bounds')]
    sum: Annotated[float | int, Field(title='Sum')]
    min: Annotated[float | int, Field(title='Min')]
    max: Annotated[float | int, Field(title='Max')]


class V1Alpha1MetricsCountValue(BaseModel):
    attributes: Annotated[dict[str, Any], Field(title='Attributes')]
    start_time_unix_nano: Annotated[int, Field(title='Start Time Unix Nano')]
    time_unix_nano: Annotated[int, Field(title='Time Unix Nano')]
    value: Annotated[float | int, Field(title='Value')]


class V1Alpha1Metrics(
    BaseSchema,
    RootModel[
        dict[str, list[V1Alpha1MetricsCountValue | V1Alpha1MetricsBucketValue]] | None
    ],
):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.ai.metrics.v1alpha1+json"
