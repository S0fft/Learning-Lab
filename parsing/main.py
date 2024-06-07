from time import sleep

import requests
from bs4 import BeautifulSoup

DOMAIN_NAME = "https://scrapingclub.com"

list_card_url = []


for page in range(1, 8):
    sleep(3)
    url = f"https://scrapingclub.com/exercise/list_basic/?page={page}"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find_all("div", class_="w-full rounded border")

    for i in data:
        card_url = DOMAIN_NAME + i.find("a").get("href")
        list_card_url.append(card_url)


for url in list_card_url:
    url = f"https://scrapingclub.com/exercise/list_basic/?page={page}"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find_all("div", class_="w-full rounded border")

    for i in data:
        card_url = DOMAIN_NAME + i.find("a").get("href")
        list_card_url.append(card_url)

