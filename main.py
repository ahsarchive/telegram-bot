import logging
from aiogram import Bot, Dispatcher, types, executor

API_TOKEN = "7608238885:AAGXJssAS10kRF0azpVYZ-19GZWrXKxGE3Q"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(f"Принято: {message.text}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
