from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config

bot = Bot(config("TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.message):
    await bot.send_message(
        message.chat.id,
        'Hi! I\'m bot that will help you find some goods on <b><a href="https://rozetka.com.ua/ua/">Rozetka</a></b>',
        parse_mode="html",
        disable_web_page_preview=1
    )

executor.start_polling(dp)
