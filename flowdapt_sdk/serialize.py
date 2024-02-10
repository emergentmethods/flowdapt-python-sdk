import orjson
from typing import Any


def serialize(data: Any) -> bytes:
    return orjson.dumps(data)

def deserialize(data: bytes) -> Any:
    return orjson.loads(data)
