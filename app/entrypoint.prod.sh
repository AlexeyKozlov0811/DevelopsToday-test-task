#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

CMD python manage.py makemigrations --no-input
CMD python manage.py migrate
CMD gunicorn app.wsgi:application --bind 0.0.0.0:$PORT

exec "$@"
