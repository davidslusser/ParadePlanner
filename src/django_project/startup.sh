#!/bin/sh
pwd
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py add_superuser --username admin --group admin --password $ADMINPWD
gunicorn core.wsgi
