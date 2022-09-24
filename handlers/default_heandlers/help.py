from loader import dp
from aiogram.types import Message
from my_logger.loger import logger


@dp.message_handler(commands=['help'], state='*')
async def welcome(message: Message):
    logger.info(f'Пользователь {message.from_user.full_name} ввел команду /help')
    await message.answer(f'Для запуска начала диалога нажмите /start')

