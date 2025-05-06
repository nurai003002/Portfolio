#!/bin/sh


# Подождите, пока база данных будет доступна
until nc -z -v -w30 db_renx 5432
do
  echo "Waiting for database connection..."
  sleep 5
done

python manage.py makemigrations

# Выполните миграции
python manage.py migrate

# Соберите статические файлы
python manage.py collectstatic --noinput

# Запустите команду (gunicorn)
exec "$@"