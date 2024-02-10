from __future__ import annotations
from uuid import UUID, uuid4
from typing import Annotated
from datetime import datetime

from flowdapt_sdk._compat import BaseModel, Field


class V1Alpha1ResourceMetadata(BaseModel):
    uid: Annotated[UUID, Field(default_factory=uuid4, title='Uid')]
    name: Annotated[str, Field(title='Name')]
    created_at: Annotated[datetime, Field(default_factory=datetime.utcnow, title='Created At')]
    updated_at: Annotated[datetime, Field(default_factory=datetime.utcnow, title='Updated At')]
    annotations: Annotated[dict[str, str], Field(title='Annotations')] = {}
