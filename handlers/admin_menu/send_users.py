from aiogram.types import CallbackQuery
from database.models import Users
import csv


async def send_users(call: CallbackQuery):
    from handlers.admin_menu.admin_menu import admin_menu

    file ='database/all_users.csv'
    with open(file, mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter="#", lineterminator="\r")
        file_writer.writerow(['id пользователя', 'Имя пользователя', 'Баланс'])
        all_users_info = Users.select()
        for user in all_users_info:
            file_writer.writerow([user.user_id, user.user_name, user.balance])

    await call.message.answer_document(open(file, "rb"))

    await admin_menu(call.message)
