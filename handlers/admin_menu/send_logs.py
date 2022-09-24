from aiogram.types import CallbackQuery
import os
from my_logger.loger import logger


async def send_logs(call: CallbackQuery):
    from handlers.admin_menu.admin_menu import admin_menu
    for file in os.listdir('my_logger/logs'):
        dir_file = f'my_logger/logs/{file}'
        if os.stat(dir_file).st_size == 0:
            await call.message.answer(f'В файле {file} нет записей')
        else:
            await call.message.answer_document(open(dir_file, "rb"))

    logger.info(f'Администратор {call.message.from_user.full_name} выполнил выгрузку логов')
    await admin_menu(call.message)
