from typing import Iterable, Any
from urllib.parse import urljoin, urlencode

from flowdapt_sdk._compat import BaseModel, validate_model
from flowdapt_sdk.dto.base import BaseSchema


def build_version_header(resource_type: str, version: str) -> str:
    return f"{resource_type}.{version}"


def build_accept_header(accepted_types: list[tuple[str, float]]) -> str:
    accept_strings = []
    for content_type, quality in accepted_types:
        quality = f"; q={quality}" if quality < 1.0 else ""
        accept_strings.append(f"{content_type}{quality}")
    return ", ".join(accept_strings)


def build_url(
    base_url: str,
    path: str,
    query: dict | None = None,
    params: dict | None = None,
) -> str:
    params = {k: str(v) for k, v in (params or {}).items()}
    path = path.format(**params)
    url = urljoin(base_url, path)

    if query:
        query_parts = []
        for k, v in query.items():
            if v is None:
                continue
            if isinstance(v, Iterable) and not isinstance(v, str):
                query_parts.extend([(k, str(item)) for item in v])
            else:
                query_parts.append((k, str(v)))
        url += "?" + urlencode(query_parts, doseq=True)

    return url


def determine_content_type(body: Any) -> str:
    if hasattr(body, "content_type"):
        return body.content_type
    elif isinstance(body, bytes):
        return "application/octet-stream"
    elif isinstance(body, dict):
        return "application/json"
    else:
        return "text/plain"


def get_latest_version(dto_map: dict[str, tuple]):
    return list(dto_map.keys())[-1]


def build_request_data(
    dto_map: dict[str, tuple[BaseModel | None, BaseModel]],
    data: Any | None = None,
    version: str | None = None,
) -> tuple[BaseModel, Any, str]:
    if not version:
        if data and isinstance(data, BaseSchema):
            version = data.__version__
        else:
            version = get_latest_version(dto_map)

    (request_dto, response_dto) = dto_map[version]

    if data:
        if isinstance(data, dict) and request_dto:
            data = validate_model(request_dto, data)

            if version and not data.__version__ == version:
                raise ValueError(
                    f"Version mismatch in payload model: {data.__version__} != {version}"
                )

    return (response_dto, data, version)
