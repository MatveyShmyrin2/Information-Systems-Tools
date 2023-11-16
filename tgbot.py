#!C:\Apache24\htdocs\venv\Scripts\python.exe

from aiogram import Bot, Dispatcher, executor, types
token = '6256736277:AAHa6uk-r2Cp7YXNK4aUzJ7ZCmLnqepBxeY'
bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши что-нибудь!")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Я умею переворачивать слова!")

@dp.message_handler ()
async def answer_message(message:types.Message):
    a = message.text[::-1]
    await message.reply(a.lower())

if __name__ == '__main__':
    executor.start_polling(dp)


