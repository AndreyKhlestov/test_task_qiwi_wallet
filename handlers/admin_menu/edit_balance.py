from loader import dp
from my_logger.loger import logger
from states.user_states import UserState
from aiogram.types import Message
from database.models import Users
from aiogram.dispatcher import FSMContext
from utils.check_num import check_num


async def edit_balance_user(message: Message, user_id: int):
    await UserState.input_edit_balance.set()
    user_inf = Users.select().where(Users.user_id == user_id).get()
    await message.answer(f'У пользователя {user_inf.user_name} (id = {user_id}) на балансе {user_inf.balance} руб.\n'
                         f'Какую сумму вы хотите установить пользователю?')


@dp.message_handler(state=UserState.input_edit_balance)
async def check_user_id(message: Message, state: FSMContext):
    from handlers.admin_menu import admin_menu
    check = check_num(message.text)  # проверка - является ли введенный текст подходящим критериям числом
    if isinstance(check, float):
        user_id = (await state.get_data())['user_id']
        new_balance = check
        Users.update(balance=new_balance).where(Users.user_id == user_id).execute()
        await message.answer(f'Баланс изменен.\n'
                             f'Теперь у пользователя на балансе {new_balance} руб.')
        await admin_menu(message)
    else:
        logger.info(f'Администратор {message.from_user.full_name} ввел некорректную сумму')
        await message.answer(check)
