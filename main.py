import requests

from bs4 import BeautifulSoup

product = input()


def search_posts():
    url = "https://habr.com/ru/search/?q=" + product + "%20&target_type=posts&order=date"
    request = requests.get(url)
    bs = BeautifulSoup(request.text, "html.parser")

    all_links = bs.find_all("a", class_="tm-article-snippet__title-link")

    for link in all_links:
         print("https://habr.com" + link["href"])


def last_news():
    url = 'https://habr.com/ru/news/'
    request = requests.get(url)
    bs = BeautifulSoup(request.text, "html.parser")
    all_links = bs.find_all("a", class_="tm-article-snippet__title-link")
    for link in all_links:
        print("https://habr.com" + link["href"])
