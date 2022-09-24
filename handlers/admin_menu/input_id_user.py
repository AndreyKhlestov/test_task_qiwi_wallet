from loader import dp
from states.user_states import UserState
from aiogram.types import Message, CallbackQuery
from database.models import Users
from aiogram.dispatcher import FSMContext
from handlers.admin_menu.edit_balance import edit_balance_user
from handlers.admin_menu.block_user import block_user
from config import DEFAULT_COMMANDS


async def input_id_user(call: CallbackQuery):
    await call.message.answer('Введите id пользователя')


@dp.message_handler(lambda message: message.text not in DEFAULT_COMMANDS,
                    state=[UserState.edit_balance, UserState.block_user])
async def check_user_id(message: Message, state: FSMContext):
    text = message.text
    if text.isdigit():
        user_id = int(text)

        user_info = Users.select().where(Users.user_id == user_id)

        if len(user_info) == 0:
            await message.answer('Пользователя с таким id нет.\nВведите правильный id пользователя')

        elif await state.get_state() == 'UserState:edit_balance':
            await state.update_data(user_id=user_id)  # Сохранение id в состояние пользователя
            await edit_balance_user(message, user_id)

        elif await state.get_state() == 'UserState:block_user':
            await block_user(message, user_id)

    else:
        await message.answer('id пользователя должен состоять только из чисел (без пробелов)')
