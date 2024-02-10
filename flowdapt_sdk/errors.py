class APIError(Exception):
    status_code: int = 500

    def __init__(self, detail: str, status_code: int | None = None) -> None:
        self.status_code = status_code or self.status_code
        self.detail = detail

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self.status_code} - {self.detail}"


class BadRequestError(APIError):
    status_code = 400


class ResourceNotFoundError(APIError):
    status_code = 404


class UnauthorizedError(APIError):
    status_code = 401


class ForbiddenError(APIError):
    status_code = 403


class MethodNotAllowed(APIError):
    status_code = 405


class ValidationError(APIError):
    status_code = 422
    detail: dict

    def __init__(self, detail: dict, status_code: int | None = None) -> None:
        self.status_code = status_code or self.status_code
        self.detail = detail


ErrorMap = {
    400: BadRequestError,
    401: UnauthorizedError,
    403: ForbiddenError,
    404: ResourceNotFoundError,
    405: MethodNotAllowed,
    422: ValidationError,
    500: APIError,
}

def raise_from_json(json: dict) -> None:
    status_code = json.get("status_code")
    detail = json.get("detail")

    raise ErrorMap.get(status_code, APIError)(detail, status_code)
