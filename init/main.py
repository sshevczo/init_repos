import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN: str = "6184236578:AAG4cWJcP7mxym4DSv76O2wy6i_94icFutA"


logging.basicConfig(level=logging.INFO)

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def procces_start_command(message: types.Message):
    await message.answer("Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.answer(' Ира , привет!)')


@dp.message_handler()
async def send_echo(message: types.Message):
    await message.reply(text=message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
