import time
from celery import shared_task, task
from .scrapers import scrape

URL = "https://dev.to/search?q=django"


@task
def scrape_dev_to():
    scrape(URL)
    return


@shared_task
def scrape_async():
    scrape(URL)
    return
