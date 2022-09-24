from loader import dp
from aiogram.types import Message
from states.user_states import UserState


@dp.message_handler(state=UserState.finish)
@dp.message_handler(state='*')
async def echo(message: Message):
    """Эхо хендлер, куда летят неизвестные команды и текстовые сообщения без указанного состояния"""
    await message.answer(f'"{message.text}" - неизвестная команда.\n'
                         f'Введите команду /start для начала диалога')
