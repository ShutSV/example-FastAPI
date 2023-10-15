from src.database import User
from src.tasks import log_user_db
from src.utils import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User

    @classmethod
    def add(cls, user):
        with cls.session() as s:
            try:
                s.add(user)
                s.commit()
                log_user_db.delay("HTTP_201, пользователь добавлен")
            except Exception as e:
                log_user_db.delay(f"Postgres error: {e}")
                print(f"Ошибка добавления пользователя: {e}")
