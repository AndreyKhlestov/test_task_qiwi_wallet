from loader import dp
from my_logger.loger import logger
from aiogram.types import Message
from config import id_admin
from handlers.admin_menu.admin_menu import admin_menu


@dp.message_handler(commands=['admin'], state='*')
async def admin(message: Message):
    logger.info(f'Пользователь {message.from_user.full_name} ввел команду /admin')
    if id_admin == message.from_user.id:
        await admin_menu(message)
