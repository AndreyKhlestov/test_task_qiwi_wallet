from loader import dp
from keyboards.default_inline_keyboards import inline_keyboards
from log.loger import logger
from states.user_states import UserState
from aiogram.types import Message, CallbackQuery


@dp.message_handler(commands=['start'])
async def start(message: Message):
    logger.info(f'Пользователь {message.from_user.full_name} запустил бота')
    await UserState.start.set()
    await message.answer(f'Привет, {message.from_user.full_name}')

    directions_list = ['Пополнить баланс']
    keyboards = inline_keyboards(directions_list)
    await message.answer(
        f'Я - бот для пополнения баланса.\n'
        f'Нажмите на кнопку, чтобы пополнить баланс',
        reply_markup=keyboards
    )


@dp.callback_query_handler(state=UserState.start)
async def refill_button(call: CallbackQuery):
    logger.info(f'Пользователь {call.message.from_user.full_name} нажал на кнопку "пополнить баланс"')
    await UserState.next()
    await call.message.edit_text(f'Введите сумму, на которую вы хотите пополнить баланс')


@dp.message_handler(state=UserState.start)
async def start(message: Message):
    logger.info(f'Пользователь {message.from_user.full_name} написал боту вместо нажатия кнопки "Пополнить баланс"')

    await message.answer('Пожалуйста, нажмите на кнопку "Пополнить баланс" под сообщением выше')
