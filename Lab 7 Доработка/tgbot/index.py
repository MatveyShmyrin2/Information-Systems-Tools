#!C:\Apache24\htdocs\venv\Scripts\python.exe
import hashlib
from aiogram import Bot, Dispatcher, executor, types

token = '6256736277:AAHa6uk-r2Cp7YXNK4aUzJ7ZCmLnqepBxeY'
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    """
    Приветствие пользователя
    """
    await message.reply("Привет!\nНапиши что-нибудь!")


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Я умею отправлять SHA256 хэш по строке!")


@dp.message_handler()
async def answer_message(message: types.Message):
    my_hash = hashlib.sha256(message.text.encode('utf-8')).hexdigest()
    await message.reply(my_hash)


def func():
    """
    Some description
    """
    print('Test')


if __name__ == '__main__':
    executor.start_polling(dp)
