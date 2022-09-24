from loader import dp
from aiogram.types import Message, CallbackQuery
from keyboards.default_inline_keyboards import inline_keyboards
from loader import p2p
from pyqiwip2p.p2p_types.errors import QiwiError
from aiogram.dispatcher import FSMContext
from states.user_states import UserState
# from config import banned_users
from database.models import Users

# a = set()
# a.add(465654693)
# a.add(465654993)
# a.add(4656693)
# a.add(45654693)




# from . import handle_banned
# from . import admin
# from . import help
# from . import start
#
# from . import test
#
# from . import admin_menu
# from . import input_id_user
# from . import edit_balance
# from . import block_user
# from . import send_users
# from . import send_logs
#
# from . import main_menu
# from . import refill

@dp.message_handler(commands=['test'], state='*')
async def start(message: Message, state: FSMContext):
    if message.from_user.id == 427346264:

        print(await state.get_state())
    elif message.from_user.id == 465654693:
        user_id = 427346264

        # state = dp.current_state(chat=user_id, user=user_id)
        # await state.set_state(UserState.ban)

        await dp.current_state(chat=user_id, user=user_id).set_state(UserState.ban)
        print('смена состояния на бан')


    # a = await state.get_state()
    # if a:
    #     await message.answer(a)
    # else:
    #     await message.answer('None')
    #
    # await message.answer(f'{message.chat.id}, {message.from_user.id}')
    # await dp.current_state(user=message.from_user.id).set_state(UserState.ban)
    # # await my_sate.set_state(UserState.ban)
    #
    # a = await state.get_state()
    # if a:
    #     await message.answer(a)
    # else:
    #     await message.answer('None')

# state = dp.current_state(chat=chat_id, user=user_id)
# await state.set_state(User.accepted)
# Где:
# dp - объект класса Dispatcher
# chat_id - id чата, который должен быть равен id пользователя, если это переписка с пользователем
# User.accepted - состояние в которое мы хотим привести пользователя


# @dp.callback_query_handler(user_id=a, state='*')
# async def handle_banned(call: CallbackQuery):
#     print(f"{call.from_user.full_name} пишет, но мы ему не ответим!")
#     return True

# @dp.message_handler(user_id=a)
# async def handle_banned(msg: Message):
#     print(f"{msg.from_user.full_name} пишет, но мы ему не ответим!")
#     return True




