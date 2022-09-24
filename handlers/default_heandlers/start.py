from loader import dp
from my_logger.loger import logger
from states.user_states import UserState
from aiogram.types import Message
from handlers.user_menu.main_menu import main_menu
from config import id_admin
from handlers.default_heandlers.admin import admin
from database.models import Users


@dp.message_handler(commands=['start'], state='*')
async def start(message: Message):
    await UserState.start.set()

    user_name = message.from_user.full_name
    user_id = message.from_user.id
    user_info = Users.select().where(Users.user_id == user_id)

    logger.info(f'Пользователь {user_name} запустил бота')

    if len(user_info) == 0:
        logger.info(f'Новый пользователь {user_name} добавлен в базу')
        Users.create(user_id=user_id, user_name=user_name, balance=0, block=False)

    await message.answer(f'Привет, {user_name}\n'
                         f'Я - бот для пополнения баланса.')

    if id_admin == user_id:
        await admin(message)
    else:
        await main_menu(message)
