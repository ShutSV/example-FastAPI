from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from .offers import router as offers_router
from .users import router as users_router


router = APIRouter(prefix="/v1", default_response_class=ORJSONResponse)
router.include_router(router=offers_router)
router.include_router(router=users_router)
