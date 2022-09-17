from loader import dp
from aiogram.types import Message


@dp.message_handler(commands=['help'])
async def welcome(message: Message):
    await message.answer(
        f'Для запуска главного меню нажмите /start')
