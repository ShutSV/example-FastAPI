from starlette.authentication import AuthCredentials, BaseUser
from starlette.middleware.authentication import AuthenticationBackend, AuthenticationMiddleware
from starlette.requests import HTTPConnection

from src.repositories import UserRepository
from src.settings import settings
from src.utils import verify_access_token


class UserInfo(BaseUser):
    def __init__(self, pk: str, email: str):
        self.pk = pk
        self.email = email

    @property
    def is_authenticated(self) -> bool:
        return True

    @property
    def identity(self) -> str:
        return self.pk

    @property
    def display_role(self) -> str:
        return self.email


class JWTAuthenticationBackend(AuthenticationBackend):
    async def authenticate(
            self, conn: HTTPConnection
    ) -> tuple[AuthCredentials, UserInfo] | None:
        auth = conn.headers.get("Authorization") \
            if 'Authorization' in conn.headers \
            else conn.headers.get("authorization")

        if not auth or not auth.startswith(f"{settings.TOKEN_TYPE}"):
            return

        token = auth.replace(f"{settings.TOKEN_TYPE} ", "")

        payload = verify_access_token(token=token)

        if not payload:
            return

        user = UserRepository.filter(id=payload.get("sub")).first()

        if not user:
            return

        return AuthCredentials(["authenticated"]), UserInfo(
            pk=user.id,
            email=user.email
        )


MIDDLEWARES = (
    (AuthenticationMiddleware, {'backend': JWTAuthenticationBackend()}),
)
