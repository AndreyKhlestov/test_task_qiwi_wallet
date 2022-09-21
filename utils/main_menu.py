from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from states.user_states import UserState


async def main_menu(message: Message):
    await UserState.next()
    keyboard = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text='Пополнить баланс', callback_data='Пополнить баланс')
    keyboard.add(button)
    await message.answer(f'Нажмите на кнопку, чтобы пополнить баланс', reply_markup=keyboard)
