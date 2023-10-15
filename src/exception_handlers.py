from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from starlette.requests import Request


def validation_error_handler(request: Request, exc: RequestValidationError) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"detail": [{"msg": e.get('msg'), "input": e.get('input')} for e in exc.errors()]}
    )
