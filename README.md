# QRkot

## Описание

**QRkot** - это API сервиса по сбору средств для финансирования благотворительных проектов.

### Реализованный API функционал:

1. Регистрация пользователей
2. Создание благотворительных проектов
3. Создание пожертвований
4. Автоматическое распределение пожертвований по проектам

Также реализовано автоматическое создание суперпользователя при первом запуске проекта

## Используемые технологии

- [Python](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pypi.org/project/pydantic/)
- [SQLAlchemy](https://pypi.org/project/SQLAlchemy/)
- [Alembic](https://pypi.org/project/alembic/)

## Установка и запуск

1. Клонировать репозиторий:

```
git clone git@github.com:S-Sagalov/cat_charity_fund.git
```

2. Активировать виртуальное окружение и установить зависимости:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Создать в корневой директории файл .env со следующим наполнением:

```
APP_TITLE=QRKot
DATABASE_URL=sqlite+aiosqlite:///./{название базы данных}.db
SECRET={секретное слово}
FIRST_SUPERUSER_EMAIL={email суперюзера}
FIRST_SUPERUSER_PASSWORD={пароль суперюзера}
```

4. Применить миграции для создания базы данных:

```
alembic upgrade head
```

5. Запустить проект:

```
uvicorn app.main:app --reload
```

Сервис будет запущен и доступен по следующим адресам:
- http://127.0.0.1:8000 - API
- http://127.0.0.1:8000/docs - автоматически сгенерированная документация Swagger
- http://127.0.0.1:8000/redoc - автоматически сгенерированная документация ReDoc

Ознакомить с доступными эндпоинтами можно в приведённой выше документации

Автор: [SSagalov](https://github.com/S-Sagalov)

Студент кагорты 19+ Яндекс Практикум
