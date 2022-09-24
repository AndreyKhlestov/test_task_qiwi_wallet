from aiogram.types import Message
from loader import dp
from database.models import Users
# from config import banned_users
# from handlers.handle_banned import banned_users
from states.user_states import UserState
from config import id_admin


async def block_user(message: Message, user_id: int):
    from handlers.admin_menu.admin_menu import admin_menu
    user_inf = Users.select().where(Users.user_id == user_id).get()
    first_text = f'Пользователь {user_inf.user_name} (id = {user_id})'
    if user_inf.block:
        await message.answer(f'{first_text} уже был(а) заблокирован(а)')

    elif user_id == id_admin:
        await message.answer('Невозможно заблокировать администратора (себя)')

    else:
        Users.update(block=True).where(Users.user_id == user_id).execute()
        await dp.current_state(chat=user_id, user=user_id).set_state(UserState.ban)
        await message.answer(f'{first_text} заблокирован(а)')

    await admin_menu(message)
