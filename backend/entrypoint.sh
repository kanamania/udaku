#!/bin/sh

if [ "$DATABASE" = "mysql" ]
then
    echo "Waiting for mysql..."

    while ! nc -z $SQL_HOST_MYSQL $SQL_PORT_MYSQL; do
      sleep 0.1
    done

    echo "MySQL started"
fi

#python manage.py flush --no-input
python manage.py makemigrations
python manage.py migrate

exec "$@"