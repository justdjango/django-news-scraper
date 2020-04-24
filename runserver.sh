#!/bin/sh

python manage.py migrate
python manage.py makesuper
gunicorn demo.wsgi --bind=0.0.0.0:80