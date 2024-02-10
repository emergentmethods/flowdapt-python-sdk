from __future__ import annotations

from typing import Annotated

from flowdapt_sdk._compat import BaseModel, Field


class APIErrorModel(BaseModel):
    status_code: Annotated[int | None, Field(title='Status Code')] = 500
    detail: Annotated[str | None, Field(title='Detail')] = "string"


class ValidationError(BaseModel):
    loc: Annotated[list[str | int], Field(title='Location')]
    msg: Annotated[str, Field(title='Message')]
    type: Annotated[str, Field(title='Error Type')]


class HTTPValidationError(BaseModel):
    detail: Annotated[list[ValidationError] | None, Field(title='Detail')] = None
