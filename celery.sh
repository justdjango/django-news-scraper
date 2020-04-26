#!/bin/sh

celery -A newsscraper worker --beat --scheduler django_celery_beat.schedulers:DatabaseScheduler -l info