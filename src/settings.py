from celery import Celery
from passlib.context import CryptContext
from pydantic import PostgresDsn, RedisDsn, SecretStr
from pydantic_settings import BaseSettings
from redis.asyncio import Redis


class Settings(BaseSettings):
    DB_URL: PostgresDsn
    REDIS_URL: RedisDsn
    CELERY_RESULT_BACKEND: RedisDsn
    CELERY_BROKER_URL: RedisDsn
    TOKEN_TYPE: str
    ALGORITHM: str
    ACCESS_EXP_TOKEN: int
    REFRESH_EXP_TOKEN: int
    SECRET_STR: SecretStr


settings = Settings()
celery = Celery()
celery.config_from_object(obj=settings, namespace='CELERY')
celery.autodiscover_tasks(packages=['src'])
redis = Redis.from_url(url=settings.REDIS_URL.unicode_string())
pwd_context = CryptContext(schemes=['bcrypt'])
