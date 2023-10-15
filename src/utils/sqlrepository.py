from sqlalchemy import update, delete

from src.database.base import Base
from .repositories import AbstractRepository


class SQLAlchemyRepository(AbstractRepository):
    model: Base
    session = Base.session

    @classmethod
    def get(cls, pk):
        with cls.session() as s:
            return s.get(cls.model, pk)

    @classmethod
    def all(cls):
        with cls.session() as s:
            return s.query(cls.model)

    @classmethod
    def filter(cls, **kwargs):
        with cls.session() as s:
            return s.query(cls.model).filter_by(**kwargs)

    @classmethod
    def add(cls, instance):
        with cls.session() as s:
            s.add(instance)
            s.commit()

    @classmethod
    def update(cls, pk, **kwargs):
        with cls.session() as s:
            s.execute(update(cls.model).filter_by(id=pk).values(**kwargs))
            s.commit()

    @classmethod
    def delete(cls, pk):
        with cls.session() as s:
            s.execute(delete(cls.model).filter_by(id=pk))
            s.commit()
