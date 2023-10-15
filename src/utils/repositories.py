from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    @classmethod
    @abstractmethod
    def get(cls, pk):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def all(cls):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def filter(cls, **kwargs):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def add(cls, instance):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def update(cls, pk, **kwargs):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def delete(cls, pk):
        raise NotImplementedError
