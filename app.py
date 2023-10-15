from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi.exceptions import RequestValidationError
from sqladmin import Admin
from sqlalchemy import create_engine

from src.admin import AdminUserDB, AdminOfferDB
from src.api import api_router
from src.exception_handlers import validation_error_handler
from src.middlewares import MIDDLEWARES
from src.settings import settings, redis
from src.types import ValidationError


app = FastAPI(responses={422: {"model": ValidationError}})
app.add_exception_handler(exc_class_or_status_code=RequestValidationError, handler=validation_error_handler)
app.include_router(router=api_router)

admin = Admin(app, engine=create_engine(url=settings.DB_URL.unicode_string()))
admin.add_view(AdminUserDB)
admin.add_view(AdminOfferDB)


@app.on_event("startup")
async def startup():
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

for middlewares, options in MIDDLEWARES:
    app.add_middleware(middlewares, **options)
