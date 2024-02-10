from __future__ import annotations
from typing import Optional, Any
from httpx import AsyncClient, HTTPStatusError
from enum import Enum

from flowdapt_sdk.version import __version__
from flowdapt_sdk.serialize import serialize, deserialize
from flowdapt_sdk.errors import raise_from_json
from flowdapt_sdk.utils import (
    build_accept_header,
    build_url,
    determine_content_type
)


class StreamType(str, Enum):
    bytes = "bytes"
    lines = "lines"
    raw = "raw"


class APIRequest:
    def __init__(
        self,
        base_url: str,
        method: str,
        endpoint: str,
        body: Optional[Any] = None,
        query: Optional[dict] = None,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        accept: Optional[list[tuple[str, float]]] = None,
    ) -> None:
        self.base_url = base_url
        self.method = method
        self.endpoint = endpoint
        self.query = query
        self.params = params
        self.accept = accept
        self.url = build_url(
            base_url=self.base_url,
            path=self.endpoint,
            query=self.query,
            params=self.params
        )
        self.content_type = determine_content_type(body)
        self.body = serialize(body) if body else None
        self.accept = accept or [
            (self.content_type if "json" in self.content_type else "application/json", 1.0)
        ]
        self.headers = headers or {}
        self.headers["Content-Type"] = self.headers.pop("Content-Type", self.content_type)
        self.headers["Accept"] = build_accept_header(self.accept)


class APIResponse:
    def __init__(
        self,
        request: APIRequest,
        status_code: int,
        headers: dict,
        body: bytes,
        stream: bool = False,
    ) -> None:
        self.request = request
        self.status_code = status_code
        self.headers = headers
        self.body = body
        self.stream = stream
        self.content_type = headers.get("Content-Type", "application/json")
        self.content = self.deserialize_body() if not self.stream else self.body

    def deserialize_body(self) -> Any:
        if self.content_type == "application/octet-stream":
            return self.body
        elif self.content_type == "application/json":
            return deserialize(self.body)
        elif self.content_type == "text/plain":
            return self.body.decode("utf-8")
        else:
            return self.body


class APIClient:
    def __init__(
        self,
        base_url: str,
        verify_ssl: bool = True,
        retries: int = 3,
        timeout: Optional[float] = None,
        follow_redirects: bool = True,
    ) -> None:
        self.base_url = base_url
        self.verify_ssl = verify_ssl
        self.retries = retries
        self.timeout = timeout

        self._client = AsyncClient(
            base_url=self.base_url,
            verify=self.verify_ssl,
            timeout=self.timeout,
            follow_redirects=follow_redirects,
            headers={
                "User-Agent": f"flowdapt-sdk-python/{__version__}"
            }
        )

    async def close(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> APIClient:
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.close()

        if exc:
            raise exc

    def build_request(
        self,
        method: str,
        endpoint: str,
        body: Optional[Any] = None,
        query: Optional[dict] = None,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        accept: Optional[list[tuple[str, float]]] = None,
    ) -> APIRequest:
        return APIRequest(
            base_url=self.base_url,
            method=method,
            endpoint=endpoint,
            body=body,
            query=query,
            headers=headers,
            params=params,
            accept=accept,
        )

    async def request(
        self,
        method: str,
        endpoint: str,
        body: Optional[Any] = None,
        query: Optional[dict] = None,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        accept: Optional[list[tuple[str, float]]] = None,
        stream: bool = False,
        stream_type: StreamType = StreamType.bytes,
    ) -> APIResponse:
        request = self.build_request(
            method=method,
            endpoint=endpoint,
            body=body,
            query=query,
            headers=headers,
            params=params,
            accept=accept,
        )

        response = await self._client.request(
            method=request.method,
            url=request.url,
            content=request.body,
            headers=request.headers,
        )
        try:
            response.raise_for_status()
        except HTTPStatusError as e:
            raise_from_json(
                e.response.json()
            )

        if stream:
            match stream_type:
                case StreamType.bytes:
                    response_body = response.aiter_bytes()
                case StreamType.lines:
                    response_body = response.aiter_lines()
                case StreamType.raw:
                    response_body = response.aiter_raw()
        else:
            response_body = response.content

        return APIResponse(
            request=request,
            status_code=response.status_code,
            headers=dict(response.headers.items()),
            body=response_body,
            stream=stream,
        )

    async def get(
        self,
        endpoint: str,
        query: Optional[dict] = None,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        accept: Optional[list[tuple[str, float]]] = None,
        stream: bool = False,
        stream_type: StreamType = StreamType.bytes,
    ) -> APIResponse:
        return await self.request(
            "GET",
            endpoint,
            query=query,
            headers=headers,
            params=params,
            accept=accept,
            stream=stream,
            stream_type=stream_type,
        )

    async def post(
        self,
        endpoint: str,
        body: Optional[Any] = None,
        query: Optional[dict] = None,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        accept: Optional[list[tuple[str, float]]] = None,
        stream: bool = False,
        stream_type: StreamType = StreamType.bytes,
    ) -> APIResponse:
        return await self.request(
            "POST",
            endpoint,
            body=body,
            query=query,
            headers=headers,
            params=params,
            accept=accept,
            stream=stream,
            stream_type=stream_type,
        )

    async def put(
        self,
        endpoint: str,
        body: Optional[Any] = None,
        query: Optional[dict] = None,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        accept: Optional[list[tuple[str, float]]] = None,
        stream: bool = False,
        stream_type: StreamType = StreamType.bytes,
    ) -> APIResponse:
        return await self.request(
            "PUT",
            endpoint,
            body=body,
            query=query,
            headers=headers,
            params=params,
            accept=accept,
            stream=stream,
            stream_type=stream_type,
        )

    async def patch(
        self,
        endpoint: str,
        body: Optional[Any] = None,
        query: Optional[dict] = None,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        accept: Optional[list[tuple[str, float]]] = None,
        stream: bool = False,
        stream_type: StreamType = StreamType.bytes,
    ) -> APIResponse:
        return await self.request(
            "PATCH",
            endpoint,
            body=body,
            query=query,
            headers=headers,
            params=params,
            accept=accept,
            stream=stream,
            stream_type=stream_type,
        )

    async def delete(
        self,
        endpoint: str,
        body: Optional[Any] = None,
        query: Optional[dict] = None,
        headers: Optional[dict] = None,
        params: Optional[dict] = None,
        accept: Optional[list[tuple[str, float]]] = None,
        stream: bool = False,
        stream_type: StreamType = StreamType.bytes,
    ) -> APIResponse:
        return await self.request(
            "DELETE",
            endpoint,
            body=body,
            query=query,
            headers=headers,
            params=params,
            accept=accept,
            stream=stream,
            stream_type=stream_type,
        )
