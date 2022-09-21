from loader import dp
from log.loger import logger
from states.user_states import UserState
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton


@dp.message_handler(commands=['admin'])
async def admin_menu(message: Message):
    logger.info(f'Пользователь {message.from_user.full_name} зашел в панель админа')
    await UserState.admin_menu.set()

    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text='Пополнить баланс', callback_data='Пополнить баланс')
    keyboard.add(button)

    await message.answer(f'Я - бот для пополнения баланса.\n'
                         f'Нажмите на кнопку, чтобы пополнить баланс', reply_markup=keyboard)


@dp.callback_query_handler()
async def refill_button(call: CallbackQuery):
    logger.info(f'Пользователь {call.from_user.full_name} нажал на кнопку "пополнить баланс"')
    await UserState.next()
    await call.answer()
    await call.message.answer('Введите сумму, на которую вы хотите пополнить баланс')