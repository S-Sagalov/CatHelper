# CatHelper

**CatHelper** - это API сервиса по сбору средств для финансирования благотворительных проектов.

<details>
<summary>Реализованный API функционал</summary>

1. Регистрация пользователей
2. Создание благотворительных проектов
3. Создание пожертвований
4. Автоматическое распределение пожертвований по проектам
5. Возможность выгрузки статистики по проектам в Google Sheets

Также реализовано автоматическое создание суперпользователя при первом запуске проекта

</details>

<details>

<summary>Запуск проекта</summary>

1. Клонировать репозиторий:

```
git clone git@github.com:S-Sagalov/CatHelper.git
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
</details>

<details>
<summary>Стек</summary>

- [![Python](https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=Python&logoColor=3776AB&labelColor=d0d0d0)](https://www.python.org/)
- [![FastAPI](https://img.shields.io/badge/FastAPI-0.78.0-blue?style=flat-square&logo=FastAPI&logoColor=3776AB&labelColor=d0d0d0)](https://fastapi.tiangolo.com/)
- [![Pydantic](https://img.shields.io/badge/Pydantic-1.9.1-blue?style=flat-square&logo=Pydantic&logoColor=3776AB&labelColor=d0d0d0)](https://pypi.org/project/pydantic/)
- [![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4.36-blue?style=flat-square&logo=SQLAlchemy&logoColor=3776AB&labelColor=d0d0d0)](https://www.sqlalchemy.org/blog/2021/12/23/sqlalchemy-1.4.36-released/)
- [![Alembic](https://img.shields.io/badge/Alembic-1.7.7-blue?style=flat-square&logoColor=3776AB&labelColor=d0d0d0)](https://pypi.org/project/alembic/)

</details>