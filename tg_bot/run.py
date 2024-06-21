from aiogram import Bot, Dispatcher, executor, types
from decouple import config

bot = Bot(config("TOKEN"))
dp = Dispatcher(bot)

executor.start_polling(dp)
