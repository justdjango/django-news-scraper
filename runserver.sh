#!/bin/sh

python manage.py migrate
python manage.py makesuper
gunicorn newsscraper.wsgi --bind=0.0.0.0:80