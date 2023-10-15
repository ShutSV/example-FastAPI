from datetime import datetime, timedelta

from jose import jwt, JWTError

from src.settings import pwd_context, settings


def create_hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hash_password: str) -> bool:
    return pwd_context.verify(secret=password, hash=hash_password)


def create_access_token(sub: str) -> str:
    return jwt.encode(
        claims={
            'sub': sub,
            'exp': datetime.utcnow() + timedelta(minutes=settings.ACCESS_EXP_TOKEN)
        },
        key=settings.SECRET_STR.get_secret_value(),
        algorithm=settings.ALGORITHM
    )


def verify_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token=token,
            key=settings.SECRET_STR.get_secret_value(),
            algorithms=settings.ALGORITHM
        )
    except JWTError:
        return {}
    else:
        return payload
