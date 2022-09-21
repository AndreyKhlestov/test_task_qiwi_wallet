from loader import dp
from log.loger import logger
from states.user_states import UserState
from aiogram.types import Message, CallbackQuery
from utils.main_menu import main_menu


@dp.message_handler(commands=['start'])
async def start(message: Message):
    logger.info(f'Пользователь {message.from_user.full_name} запустил бота')
    await UserState.start.set()
    await message.answer(f'Привет, {message.from_user.full_name}\n'
                         f'Я - бот для пополнения баланса.')
    await main_menu(message)


# @dp.callback_query_handler(func=lambda c: c.data == 'button1')
# async def process_callback_button1(callback_query: types.CallbackQuery):

@dp.callback_query_handler(state=UserState.main_menu)
# @dp.callback_query_handler(text_contains='menu_')
# @dp.callback_query_handler(lambda call: call.data == 'c')
# @dp.callback_query_handler(text="Пополнить баланс")
async def refill_button(call: CallbackQuery):
    logger.info(f'Пользователь {call.from_user.full_name} нажал на кнопку "пополнить баланс"')
    await UserState.next()
    await call.answer()
    await call.message.answer('Введите сумму, на которую вы хотите пополнить баланс')


@dp.message_handler(state=UserState.start)
async def start(message: Message):
    logger.info(f'Пользователь {message.from_user.full_name} написал боту вместо нажатия кнопки "Пополнить баланс"')

    await message.answer('Пожалуйста, нажмите на кнопку "Пополнить баланс" под сообщением выше')
