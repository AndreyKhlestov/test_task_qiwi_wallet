from loader import dp
from my_logger.loger import logger
from states.user_states import UserState
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.default_inline_keyboards import inline_keyboards
from handlers.main_menu import main_menu


@dp.message_handler(commands=['admin'], state='*')
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

    await message.answer(f'Приветствую {message.from_user.full_name}, вы в панели администратора\n'
                         f'Выберите нужную команду:', reply_markup=keyboard)


@dp.callback_query_handler(state=UserState.admin_menu)
async def refill_button(call: CallbackQuery):
    await call.message.edit_text(call.message.text)  # Удаляем у предыдущего сообщения кнопки путем редактирования

    text = call.data  # Текст команды
    await call.message.answer(text)  # Вывод выбранной команды

    if text == 'Выход из панели админа':
        await main_menu(call.message)

    # logger.info(f'Пользователь {call.from_user.full_name} нажал на кнопку "пополнить баланс"')
    # await UserState.next()
    # await call.answer()
    # await call.message.answer('Введите сумму, на которую вы хотите пополнить баланс')
