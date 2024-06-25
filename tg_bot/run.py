import time

import requests
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from bs4 import BeautifulSoup
from decouple import config

bot = Bot(config("TOKEN"))
dp = Dispatcher(bot)

DOMEN = "https://prom.ua/"


@dp.message_handler(commands=["start"])
async def start(message: types.message):
    await bot.send_message(
        message.chat.id,
        "Hi! I'm bot that will help you find some goods on <b><a href='https://prom.ua/ua/'>PromUA</a></b>",
        parse_mode="html",
        disable_web_page_preview=0
    )


@dp.message_handler(content_types=["text"])
async def parser(message: types.message):
    headers = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    print(message.text)

    url = "https://prom.ua/ua/search?search_term=" + message.text
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.text, "html.parser")

    links = soup.find_all('a', class_='_0cNvO jwtUM', attrs={'data-qaid': 'product_link'})

    for link in links:
        print(DOMEN + link["href"] + "\n")

executor.start_polling(dp)
