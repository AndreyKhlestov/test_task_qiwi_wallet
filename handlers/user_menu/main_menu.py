from aiogram.types import Message, CallbackQuery
from states.user_states import UserState
from keyboards.default_inline_keyboards import inline_keyboards
from my_logger.loger import logger
from loader import dp
from aiogram.dispatcher import FSMContext


async def main_menu(message: Message):
    await UserState.main_menu.set()

    logger.info(f'Пользователь {message.from_user.full_name} перешел в главное меню')

    keyboard = inline_keyboards(['Пополнить баланс'])
    await message.answer(f'Нажмите на кнопку, чтобы пополнить баланс', reply_markup=keyboard)


@dp.callback_query_handler(state=UserState.main_menu)
async def refill_button(call: CallbackQuery, state: FSMContext):
    logger.info(f'Пользователь {call.from_user.full_name} нажал на кнопку "пополнить баланс"')
    await UserState.refill.set()
    await call.answer()
    await call.message.answer('Введите сумму, на которую вы хотите пополнить баланс')


@dp.message_handler(state=UserState.main_menu)
async def error_refill_button(message: Message):
    if message.text == '/admin':
        from handlers.default_heandlers.admin import admin
        await admin(message)
    else:
        logger.info(f'Пользователь {message.from_user.full_name} написал боту вместо нажатия кнопки "Пополнить баланс"')
        await message.answer('Пожалуйста, нажмите на кнопку "Пополнить баланс" под сообщением выше')