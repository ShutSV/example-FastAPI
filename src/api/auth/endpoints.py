from fastapi import APIRouter, HTTPException
from starlette import status

from src.database import User
from src.repositories import UserRepository
from src.types import TokenData, UserDetail, UserLoginForm, UserRegisterForm
from src.utils.utils_auth import create_access_token, create_hash_password, verify_password


router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post(
    path='/register',
    status_code=status.HTTP_201_CREATED,
    response_model=UserDetail,
    response_model_exclude={'password'},
    name='Регистрация пользователя'
)
async def register(form: UserRegisterForm):
    form = UserDetail(**form.model_dump(exclude={'confirm_password'}))
    user = User(**form.model_dump(exclude={'password'}))
    user.password = create_hash_password(password=form.password)
    UserRepository.add(user)
    return form


@router.post(
    path='/login',
    status_code=status.HTTP_200_OK,
    response_model=TokenData,
    name='Авторизация'
)
async def login(form: UserLoginForm):
    user = UserRepository.filter(email=form.email).first()

    if not verify_password(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='incorrect password')

    token = create_access_token(sub=user.id)
    return TokenData(
        access_token=token
    )
