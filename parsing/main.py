from time import sleep

import requests
from bs4 import BeautifulSoup

for page in range(1, 8):
    sleep(10)
    url = f"https://scrapingclub.com/exercise/list_basic/?page={page}"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find_all("div", class_="w-full rounded border")

    for i in data:
        name = i.find("h4").text
        price = i.find("h5").text
        url_image = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")

        print(name + "\n" + price + "\n" + url_image)
