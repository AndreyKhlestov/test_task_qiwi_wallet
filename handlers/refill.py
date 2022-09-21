from loader import dp
from my_logger.loger import logger
from states.user_states import UserState
from aiogram.types import Message, CallbackQuery
from utils.check_num import check_num
from config import lifetime
from loader import p2p
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext


@dp.message_handler(state=UserState.refill)
async def refill_num_money(message: Message, state: FSMContext):
    check = check_num(message.text)  # проверка - является ли введенный текст подходящим критериям числом
    if isinstance(check, float):
        num_money = check
        logger.info(f'Пользователь {message.from_user.full_name} ввел сумму {num_money} руб. для пополнения')

        new_bill = await p2p.bill(amount=num_money, lifetime=lifetime)

        await state.update_data(bill_id=new_bill.bill_id)  # Сохранение номера счета в состояние пользователя

        keyboard = InlineKeyboardMarkup()
        button_1 = InlineKeyboardButton(text='Оплата счета', url=new_bill.pay_url)
        button_2 = InlineKeyboardButton(text='Проверка платежа', callback_data='Проверка платежа')
        keyboard.add(button_1, button_2)

        await message.answer(f'Платеж на сумму {num_money} руб. успешно создан', reply_markup=keyboard)
        await UserState.next()
    else:
        logger.info(f'Пользователь {message.from_user.full_name} ввел некорректную сумму')
        await message.answer(check)


@dp.callback_query_handler(state=UserState.wait_pay)
async def check_pay(call: CallbackQuery, state: FSMContext):
    logger.info(f'Пользователь {call.from_user.full_name} проверяет оплату')
    bill_id = (await state.get_data())['bill_id']
    status = (await p2p.check(bill_id=bill_id)).status
    if status == 'WAITING':
        await call.answer('Счет ожидает оплаты', show_alert=True)
    else:
        await call.message.edit_text(call.message.text)  # Удаляем у предыдущего сообщения кнопки путем редактирования

        if status == 'PAID':
            text = 'Оплата прошла успешно'
        elif status == 'EXPIRED':
            text = 'Счет отклонен'
        else:
            text = 'Время жизни счета истекло. Счет не оплачен'

        await call.answer(text, show_alert=True)
        await UserState.next()
        await call.message.answer(text)
        await call.message.answer('Если вы хотите повторно пополнить баланс, то нажмите /start')

