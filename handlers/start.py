from loader import dp
from my_logger.loger import logger
from states.user_states import UserState
from aiogram.types import Message, CallbackQuery
from handlers.main_menu import main_menu


@dp.message_handler(commands=['start'], state=[None, UserState.finish])
async def start(message: Message):
    logger.info(f'Пользователь {message.from_user.full_name} запустил бота')
    await UserState.start.set()
    await message.answer(f'Привет, {message.from_user.full_name}\n'
                         f'Я - бот для пополнения баланса.')
    await main_menu(message)


@dp.callback_query_handler(state=UserState.main_menu)
async def refill_button(call: CallbackQuery):
    logger.info(f'Пользователь {call.from_user.full_name} нажал на кнопку "пополнить баланс"')
    await UserState.next()
    await call.answer()
    await call.message.answer('Введите сумму, на которую вы хотите пополнить баланс')


@dp.message_handler(state=UserState.start)
async def error_refill_button(message: Message):
    logger.info(f'Пользователь {message.from_user.full_name} написал боту вместо нажатия кнопки "Пополнить баланс"')
    await message.answer('Пожалуйста, нажмите на кнопку "Пополнить баланс" под сообщением выше')
