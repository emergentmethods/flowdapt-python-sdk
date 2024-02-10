from __future__ import annotations

from typing import Any, Annotated

from flowdapt_sdk._compat import BaseModel, Field
from flowdapt_sdk.dto.base import BaseSchema


class V1Alpha1SystemStatusOSInfo(BaseModel):
    name: Annotated[str, Field(title='Name')]
    version: Annotated[str, Field(title='Version')]
    release: Annotated[str, Field(title='Release')]
    machine: Annotated[str, Field(title='Machine')]


class V1Alpha1SystemStatusSystemInfo(BaseModel):
    time: Annotated[str, Field(title='Time')]
    cpu_pct: Annotated[float, Field(title='Cpu Pct')]
    memory: Annotated[int, Field(title='Memory')]
    disk_pct: Annotated[float, Field(title='Disk Pct')]
    network_io_sent: Annotated[int, Field(title='Network Io Sent')]
    network_io_recv: Annotated[int, Field(title='Network Io Recv')]
    threads: Annotated[int, Field(title='Threads')]
    fds: Annotated[int, Field(title='Fds')]
    pid: Annotated[int, Field(title='Pid')]


class V1Alpha1SystemStatus(BaseSchema):
    __version__ = "v1alpha1"
    __content_type__ = "application/vnd.flowdapt.ai.system.v1alpha1+json"

    version: Annotated[str, Field(title='Version')]
    name: Annotated[str, Field(title='Name')]
    system: V1Alpha1SystemStatusSystemInfo
    os: V1Alpha1SystemStatusOSInfo
    python: Annotated[str, Field(title='Python')]
    hostname: Annotated[str, Field(title='Hostname')]
    services: Annotated[dict[str, Any], Field(title='Services')]
    database: Annotated[str, Field(title='Database')]
