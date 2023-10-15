from pydantic import Field, EmailStr, field_validator, model_validator
from typing import Self
from ulid import new

from src.repositories import UserRepository
from src.types import DTO


class UserBasic(DTO):
    email: EmailStr
    password: str


class UserRegisterForm(UserBasic):
    name: str
    confirm_password: str

    @field_validator('email', mode='after')
    def email_uniq_validator(cls, email: str) -> str:
        user = UserRepository.filter(email=email).first()
        if user:
            raise ValueError('email is already in use')
        return email

    @model_validator(mode="after")
    def validator(self) -> Self:
        if self.password != self.confirm_password:
            raise ValueError('confirm password is not same')

        if self.name.lower() in self.password.lower():
            raise ValueError('name included in password')

        if self.email.lower().split("@")[0] in self.password.lower():
            raise ValueError('email included in password')

        return self


class UserDetail(UserBasic):
    name: str
    id: str = Field(
        default_factory=lambda: new().str,
        min_length=26,
        max_length=26,
        title="User unique identify",
        description="Universally Unique Lexicographically Sortable Identifier",
    )


class UserLoginForm(UserBasic):
    pass

    @field_validator('email', mode='after')
    def email_validator(cls, email: str) -> str:
        user = UserRepository.filter(email=email).first()
        if user is None:
            raise ValueError('user not found')
        return email
