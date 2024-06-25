import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from decouple import config

TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()


def register_handlers(dp: Dispatcher):
    dp.message.register(start, Command(commands=['start']))


async def start(message: Message):
    await message.answer(
        'Hi! I\'m bot that will help you find some goods on <b><a href="https://rozetka.com.ua/ua/">Rozetka</a></b>!',
        parse_mode="HTML",
        disable_web_page_preview=True
    )


async def main():
    register_handlers(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
