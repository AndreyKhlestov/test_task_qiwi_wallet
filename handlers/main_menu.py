from aiogram.types import Message
from states.user_states import UserState
from keyboards.default_inline_keyboards import inline_keyboards
from my_logger.loger import logger


async def main_menu(message: Message):
    await UserState.main_menu.set()

    logger.info(f'Пользователь {message.from_user.full_name} перешел в главное меню')

    keyboard = inline_keyboards(['Пополнить баланс'])
    await message.answer(f'Нажмите на кнопку, чтобы пополнить баланс', reply_markup=keyboard)
