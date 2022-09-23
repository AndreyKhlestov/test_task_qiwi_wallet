from loader import dp
from my_logger.loger import logger
from states.user_states import UserState
from aiogram.types import Message, CallbackQuery
from keyboards.default_inline_keyboards import inline_keyboards
from handlers.main_menu import main_menu
from handlers.admin_menu.send_logs import send_logs
from handlers.admin_menu.send_users import send_users
from handlers.admin_menu.input_id_user import input_id_user


@dp.message_handler(commands=['admin'], state='*')
async def start_admin_menu(message: Message):
    logger.info(f'Пользователь {message.from_user.full_name} зашел в панель админа')
    await admin_menu(message)


async def admin_menu(message: Message):
    await UserState.admin_menu.set()
    buttons = ['Выгрузка пользователей',
               'Выгрузка логов',
               'Изменить баланс пользователя',
               'Блокировка пользователя',
               'Выход из панели админа'
               ]
    keyboard = inline_keyboards(buttons)

    await message.answer(f'Вы в панели администратора\n'
                         f'Выберите нужную команду:', reply_markup=keyboard)


@dp.callback_query_handler(state=UserState.admin_menu)
async def refill_button(call: CallbackQuery):
    await call.message.edit_text(call.message.text)  # Удаляем у предыдущего сообщения кнопки путем редактирования

    text = call.data  # Текст команды
    await call.message.answer(text)  # Вывод выбранной команды

    if text == 'Выход из панели админа':
        logger.info(f'{call.message.from_user.full_name} вышел из панели админа')
        await main_menu(call.message)
    elif text == 'Выгрузка логов':
        logger.info(f'{call.message.from_user.full_name} выполнил выгрузку логов')
        await send_logs(call)
    elif text == 'Выгрузка пользователей':
        logger.info(f'{call.message.from_user.full_name} выполнил выгрузку пользователей')
        await send_users(call)
    elif text == 'Изменить баланс пользователя':
        await UserState.edit_balance.set()
        await input_id_user(call)
    elif text == 'Блокировка пользователя':
        await UserState.block_user.set()
        await input_id_user(call)
