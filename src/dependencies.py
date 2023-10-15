from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
from starlette.requests import Request

from .database import Base


def _get_db_session() -> Session:
    with Base.session() as s:
        yield s


def _is_authenticated(request: Request):
    if not request.user.is_authenticate:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


get_db_session = Depends(_get_db_session)
is_authenticated = Depends(_is_authenticated)
