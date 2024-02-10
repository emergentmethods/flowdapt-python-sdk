from typing import Any, TypeVar, Generic
from pydantic.version import VERSION as PYDANTIC_VERSION
from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")
IS_V1 = PYDANTIC_VERSION.startswith("1.")

if IS_V1:
    from pydantic.generics import GenericModel

    class RootModel(GenericModel, Generic[T]):
        __root__: T

        @property
        def root(self) -> T:
            return self.__root__

        @root.setter
        def root(self, value: T) -> None:
            self.__root__ = value

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}({self.__root__!s}))"

        def __str__(self) -> str:
            return self.__repr__()

        def dict(self, **kwargs) -> Any:
            return super().dict(**kwargs).get("__root__")

    validate_model = lambda cls, *args: cls.parse_obj(*args)
    _model_dump = lambda cls, *args, **kwargs: cls.dict(*args, **kwargs)
else:
    from pydantic import RootModel

    class BaseModel(BaseModel):
        model_config = ConfigDict(from_attributes=True)

    validate_model = lambda cls, *args, **kwargs: cls.model_validate(*args, **kwargs)
    _model_dump = lambda cls, *args, **kwargs: cls.model_dump(*args, **kwargs)


def model_dump(
    model: BaseModel,
    *,
    include: set[str] | set[int] | dict[int, Any] | dict[str, Any] | None = None,
    exclude: set[str] | set[int] | dict[int, Any] | dict[str, Any] | None = None,
    by_alias: bool = True,
    exclude_unset: bool = False,
    exclude_defaults: bool = False,
    exclude_none: bool = False,
) -> Any:
    return _model_dump(
        model,
        include=include,
        exclude=exclude,
        by_alias=by_alias,
        exclude_unset=exclude_unset,
        exclude_defaults=exclude_defaults,
        exclude_none=exclude_none,
    )


__all__ = (
    "BaseModel",
    "RootModel",
    "Field",
    "model_dump",
)
