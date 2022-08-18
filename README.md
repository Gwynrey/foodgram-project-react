[![foodgram-project-react workflow](https://github.com/Gwynrey/foodgram-project-react/actions/workflows/main.yml/badge.svg)](https://github.com/Gwynrey/foodgram-project-react/actions/workflows/main.yml)
# Проект Foodgram
Foodgram, «Продуктовый помощник».
Онлайн-сервис и API для него. На этом сервисе пользователи после регистрации могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать список продуктов, необходимых для приготовления выбранных блюд.

Проект доступен по следующему адресу: <http://51.250.17.153/recipes/>

Админка (login: gwynrey@mail.com pass: gwynrey) - <http://51.250.17.153/admin/>


### Технологии
- Python 3.7
- Django 3.2.13
 - Gunicorn
 - Nginx
 - Docker
 - PostgreSQL


# Запуск приложения в контейнерах Docker
Клонируйте проект:

```bash
git clone https://github.com/gwynrey/foodgram-project-react.git

```
Перейдите в папку infra, создайте .env файл (пример ниже) и выполните команду, что бы собрать контейнер:
```bash
docker-compose up -d
```
Далее выполните следующие команды:

```bash
sudo docker-compose exec backend python manage.py makemigrations
sudo docker-compose exec backend python manage.py migrate --noinput
sudo docker-compose exec backend python manage.py createsuperuser
sudo docker-compose exec backend python manage.py collectstatic --no-input
```

Также можно наполнить DB ингредиентами и тэгами:

```bash
sudo docker-compose exec backend python manage.py load_tags
sudo docker-compose exec backend python manage.py load_ingridients
```

## Шаблон наполнения env-файла

    SECRET_KEY=<seckret_key>
    ALLOWED_HOSTS=<allowed HOSTs>
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=123456
    DB_HOST=db
    DB_PORT=5432