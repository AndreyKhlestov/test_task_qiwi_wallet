from loader import dp
from keyboards.default_inline_keyboards import inline_keyboards
from log.loger import logger
from states.user_states import UserState
from aiogram.types import Message


@dp.message_handler(state=UserState.finish)
async def start(message: Message):
    logger.info(f'Пользователь {message.from_user.full_name} запустил бота')
    await UserState.start.set()

    directions_list = ['Пополнить баланс']
    keyboards = inline_keyboards(directions_list)
    await message.answer(
        f'Нажмите на кнопку, чтобы пополнить баланс',
        reply_markup=keyboards
    )
