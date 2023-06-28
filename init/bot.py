from aiogram import Bot, Dispatcher, executor, types

TOKEN_API = "6184236578:AAG4cWJcP7mxym4DSv76O2wy6i_94icFutA"

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)


async def on_startup(_):
    print("Я заупстился!")

@dp.message_handler()
async def count(message: types.Message):
    await message.answer(text=str(message.text.count('✅')))

# @dp.message_handler(commands=["give"])
# async def send_sticker(message: types.Message):
#     await message.answer("<em>Смотри какой котик</em> ❤️", parse_mode='HTML')
#     await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEJgqlknAHYELtNP9fosaubyH2DE14_fgACbgsAAtPzwUqZ7dmrj6JXpS8E")
#
# @dp.message_handler()
# async def send_heart(message: types.Message):
#     if message.text == "❤️":
#         await message.reply("🖤")




if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)