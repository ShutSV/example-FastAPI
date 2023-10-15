from datetime import datetime

from src.settings import celery


@celery.task()
def log_user_db(status):
    with open('out.txt', 'a', encoding='utf-8') as file:
        file.write(f"\n{datetime.now()} Попытка записи пользователя в DB Postgres. Результат со статусом {status}")


@celery.task()
def log_offer_db(status):
    with open('out.txt', 'a', encoding='utf-8') as file:
        file.write(f"\n{datetime.now()} Попытка записи offer в DB Postgres. Результат со статусом {status}")
