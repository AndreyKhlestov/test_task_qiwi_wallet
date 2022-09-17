from loader import dp
from aiogram.types import Message
from keyboards.default_inline_keyboards import inline_keyboards


@dp.message_handler(commands=['test'])
async def welcome(message: Message):
    pass



