from loader import dp
from my_logger.loger import logger
from aiogram.types import Message
from config import id_admin
from handlers.admin_menu.admin_menu import admin_menu


@dp.message_handler(commands=['admin'], state='*')
async def admin(message: Message):
    if id_admin == message.from_user.id:
        logger.info(f'Пользователь {message.from_user.full_name} зашел в панель админа')
        await admin_menu(message)
