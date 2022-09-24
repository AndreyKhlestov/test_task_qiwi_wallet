from loader import dp
from my_logger.loger import logger
from states.user_states import UserState
from aiogram.types import Message, CallbackQuery
from keyboards.default_inline_keyboards import inline_keyboards
from handlers.user_menu.main_menu import main_menu
from handlers.admin_menu.send_logs import send_logs
from handlers.admin_menu.send_users import send_users
from handlers.admin_menu.input_id_user import input_id_user


async def admin_menu(message: Message):
    logger.info(f'Пользователь {message.from_user.full_name} зашел в панель админа')
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
    command = call.data  # Текст команды
    text = call.message.text.replace('Выберите нужную команду:', f'Команда: {command}')
    await call.message.edit_text(text)  # Изменяем предыдущее сообщение

    if command == 'Выход из панели админа':
        logger.info(f'Администратор {call.message.from_user.full_name} вышел из панели админа')
        await main_menu(call.message)

    elif command == 'Выгрузка логов':
        await send_logs(call)

    elif command == 'Выгрузка пользователей':
        await send_users(call)

    elif command == 'Изменить баланс пользователя':
        await UserState.edit_balance.set()
        await input_id_user(call)

    elif command == 'Блокировка пользователя':
        await UserState.block_user.set()
        await input_id_user(call)
