from loader import dp
from my_logger.loger import logger
from states.user_states import UserState
from aiogram.types import Message
from handlers.main_menu import main_menu
from config import id_admin
from handlers.admin_menu.admin_menu import start_admin_menu
from database.models import Users


@dp.message_handler(commands=['start'])
async def start(message: Message):
    await UserState.start.set()

    user_name = message.from_user.full_name
    user_id = message.from_user.id
    user_info = Users.select().where(Users.user_id == user_id)

    if len(user_info) == 0:
        logger.info(f'Новый пользователь {user_name} добавлен в базу')
        user_info = Users.create(user_id=user_id, user_name=user_name, balance=0, block=False)

    if user_info.get().block:
        logger.info(f'Заблокированный пользователь {user_name} попытался запустить бота')
        await message.answer('Вы заблокированы')
    else:
        logger.info(f'Пользователь {user_name} запустил бота')
        await message.answer(f'Привет, {user_name}\n'
                             f'Я - бот для пополнения баланса.')

        if id_admin == user_id:
            await start_admin_menu(message)
        else:
            await main_menu(message)
