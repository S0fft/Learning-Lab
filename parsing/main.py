from time import sleep

import requests
from bs4 import BeautifulSoup

DOMAIN_NAME = "https://scrapingclub.com"


def get_url():
    for page in range(1, 8):
        url = f"https://scrapingclub.com/exercise/list_basic/?page={page}"

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find_all("div", class_="w-full rounded border")

        for i in data:
            card_url = DOMAIN_NAME + i.find("a").get("href")

            yield card_url


def fetch_card_details():

    for url in get_url():
        response = requests.get(url)
        sleep(3)
        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find("div", class_="my-8 w-full rounded border")
        name = data.find("h3", class_="card-title").text
        price = data.find("h4").text
        text = data.find("p", class_="card-description").text
        url_img = DOMAIN_NAME + data.find("img").get("src")

        yield name, price, text, url_img
        # print(name + '\n' + price + '\n' + text + '\n' + url_img + '\n  \n')
