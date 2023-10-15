from fastapi import APIRouter, status
from fastapi.responses import ORJSONResponse
from fastapi_cache.decorator import cache

from src.database import User
from src.dependencies import is_authenticated
from src.repositories import UserRepository
from src.types import UserDetail

router = APIRouter(
    prefix="/users", default_response_class=ORJSONResponse, tags=["users"]
)


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=None,
    name="Получение списка всех пользователей (запрос кэшируется)",
)
@cache(expire=120)
async def list_users():
    users = UserRepository.all().order_by(User.name)
    return [{"name": user.name, "ID": user.id} for user in users]


@router.get(
    path="/{pk}",
    dependencies=[is_authenticated],
    status_code=status.HTTP_200_OK,
    response_model=UserDetail,
    response_model_exclude="password",
    name="Получение информации о пользователе по ID (требуется авторизация)",
)
async def get_user(pk):
    return UserRepository.get(pk)
