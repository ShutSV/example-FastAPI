Мини pet-проект web-сервиса на Python 3.11 с фреймворком FastAPI
Пример использования набора технологий 2023 для бэкенда сервера предложения работы
Развернут на арендованном сервере по адресу IP:8001/
где IP = 83.222.9.79
Документация по адресу IP:8001/docs и IP:8001/redoc

Запускается  приложение из контейнеров docker
Применяемые технологии:
База данных Postgres (в отдельном контейнере)
SqlAlchemy + alembic
Кэширование запросов с использованием БД Redis (в отдельном контейнере)
Логирование в файл доступа к БД Postgres с использоанием Celery (в отдельном контейнере)
Настроена авторизация и добавление пользователей. По адресу IP/admin работает сервис admin для наполнения полей БД

Авторизация к полям БД "offer" настроена, но временно отключена

Фронтенд у приложения отсутствует
