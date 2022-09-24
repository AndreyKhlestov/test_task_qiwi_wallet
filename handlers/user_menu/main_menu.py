from aiogram.types import Message, CallbackQuery
from states.user_states import UserState
from keyboards.default_inline_keyboards import inline_keyboards
from my_logger.loger import logger
from loader import dp
from config import DEFAULT_COMMANDS


async def main_menu(message: Message):
    logger.info(f'Пользователь {message.from_user.full_name} перешел в главное меню')
    await UserState.main_menu.set()

    keyboard = inline_keyboards(['Пополнить баланс'])
    await message.answer(f'Нажмите на кнопку, чтобы пополнить баланс', reply_markup=keyboard)


@dp.callback_query_handler(state=UserState.main_menu)
async def refill_button(call: CallbackQuery):
    logger.info(f'Пользователь {call.from_user.full_name} нажал на кнопку "пополнить баланс"')
    await UserState.refill.set()
    await call.answer()
    await call.message.edit_text('Введите сумму, на которую вы хотите пополнить баланс')


@dp.message_handler(lambda message: message.text not in DEFAULT_COMMANDS, state=UserState.main_menu)
async def error_refill_button(message: Message):
    logger.info(f'Пользователь {message.from_user.full_name} написал боту вместо нажатия кнопки "Пополнить баланс"')
    await message.answer('Пожалуйста, нажмите на кнопку "Пополнить баланс" под сообщением выше')
