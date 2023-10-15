from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from .v1 import v1_router
from .auth import auth_router


router = APIRouter(
    prefix= "/api",
    default_response_class=ORJSONResponse
)
router.include_router(router=v1_router)
router.include_router(router=auth_router)