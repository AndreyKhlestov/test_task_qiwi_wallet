from loader import dp
from aiogram.types import Message


@dp.message_handler(commands=['start'])
async def welcome(message: Message):
    await message.answer(f'Привет, {message.from_user.full_name}')
    await message.answer(
        f'Я - бот для пополнения баланса.\n'
        f'Нажмите на кнопку, чтобы пополнить баланс'
    )

