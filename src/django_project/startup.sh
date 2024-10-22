#!/bin/sh
pwd
python manage.py migrate
python manage.py collectstatic --no-input
python manage.py add_superuser --username admin --group admin --password $ADMINPWD
gunicorn --workers 3 --bind 0.0.0.0 core.wsgi:application
