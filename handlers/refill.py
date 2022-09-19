from loader import dp
from log.loger import logger
from states.user_states import UserState
from aiogram.types import Message
from utils.check_num import check_num


@dp.message_handler(state=UserState.refill)
async def refill_num_money(message: Message):
    check = check_num(message.text)
    if isinstance(check, float):
        num_money = check
        logger.info(f'Пользователь {message.from_user.full_name} ввел сумму для пополнения')
        await message.answer(f'Пользователь ввел {num_money} руб.\nПереход в стартовое состояние')
        await UserState.next()

    else:
        logger.info(f'Пользователь {message.from_user.full_name} ввел некорректную сумму')
        await message.answer(check)

# QIWI_PRIV_KEY = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6InBjMm12NC0wMCIsInVzZXJfaWQiOiI3OTA5MDk1NTMzNyIsInNlY3JldCI6IjMxOWYwOGViODE1ZTA3MTQxNjM0ZTBiODRjYTBiM2ZmNmVlZmZkOTFiMWNmZTBhNDE4ODA1YzcxYmUxY2ViNzIifX0="
