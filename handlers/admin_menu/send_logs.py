from aiogram.types import CallbackQuery
from config import names_levels_log
import os


async def send_logs(call: CallbackQuery):
    from handlers.admin_menu import admin_menu
    for level in names_levels_log:
        file = f'my_logger/logs/{level}.log'
        if os.stat(file).st_size == 0:
            await call.message.answer(f'В файле {level}.log нет записей')
        else:
            await call.message.answer_document(open(file, "rb"))
    await admin_menu(call.message)
