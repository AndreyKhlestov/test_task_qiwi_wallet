from loader import dp
from aiogram.types import Message, CallbackQuery
from my_logger.loger import logger
from states.user_states import UserState
from database.models import Users

banned_users = set()
all_block_users = Users.select().where(Users.block == True)
for i_user in all_block_users:
    banned_users.add(i_user.user_id)


@dp.callback_query_handler(user_id=banned_users, state='*')
@dp.callback_query_handler(state=UserState.ban)
async def call_handle_banned(call: CallbackQuery):
    logger.info(f'Заблокированный пользователь {call.from_user.full_name} попытался нажать на inline-кнопку в боте')
    await call.answer('Вы заблокированы', show_alert=True)


@dp.message_handler(user_id=banned_users, state='*')
@dp.message_handler(state=UserState.ban)
async def message_handle_banned(message: Message):
    logger.info(f'Заблокированный пользователь {message.from_user.full_name} попытался написать боту')
    await message.answer('Вы заблокированы')
