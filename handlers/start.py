from loader import dp
from aiogram.types import Message
from keyboards.default_inline_keyboards import inline_keyboards
from log.loger import logger


@dp.message_handler(commands=['start'])
async def welcome(message: Message):
    logger.info(f'Пользователь {message.from_user.full_name} запустил бота')

    await message.answer(f'Привет, {message.from_user.full_name}')

    directions_list = ['Пополнить баланс']
    keyboards = inline_keyboards(directions_list)
    await message.answer(
        f'Я - бот для пополнения баланса.\n'
        f'Нажмите на кнопку, чтобы пополнить баланс',
        reply_markup=keyboards
    )

