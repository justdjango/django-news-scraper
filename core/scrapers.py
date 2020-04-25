import requests
import time
from bs4 import BeautifulSoup


def scrape(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    time.sleep(10)
    results = soup.find_all(_class="single-article single-article-small-pic")
    print(results)
    return soup
