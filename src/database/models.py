from sqlalchemy import (
    BOOLEAN,
    Column,
    CHAR,
    NUMERIC,
    TEXT,
    VARCHAR,
)
from ulid import new

from .base import Base


class User(Base):
    id = Column(CHAR(26), primary_key=True, default=lambda: new().str)
    name = Column(VARCHAR(64), nullable=False)
    email = Column(VARCHAR(256), nullable=False, unique=True)
    password = Column(VARCHAR(128), nullable=False)

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return self.__str__()


class Offer(Base):
    title = Column(TEXT, nullable=False)
    text = Column(TEXT, nullable=False)
    city = Column(VARCHAR(64), nullable=True)
    slug = Column(VARCHAR(64), nullable=False, unique=True)
    owner = Column(VARCHAR(64), nullable=False)
    cost = Column(NUMERIC, nullable=False)
    is_activated = Column(BOOLEAN, default=False)

    def __str__(self) -> str:
        return f"{self.title}"

    def __repr__(self) -> str:
        return self.__str__()
