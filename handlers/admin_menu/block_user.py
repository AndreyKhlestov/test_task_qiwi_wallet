from loader import dp
from my_logger.loger import logger
from states.user_states import UserState
from aiogram.types import Message
from database.models import Users
from aiogram.dispatcher import FSMContext
from utils.check_num import check_num


async def block_user(message: Message, user_id: int):
    from handlers.admin_menu.admin_menu import admin_menu
    user_inf = Users.select().where(Users.user_id == user_id).get()
    first_text = f'Пользователь {user_inf.user_name} (id = {user_id})'
    if user_inf.block:
        await message.answer(f'{first_text} уже был заблокирован')
    else:
        Users.update(block=True).where(Users.user_id == user_id).execute()
        await message.answer(f'{first_text} заблокирован')
    await admin_menu(message)
