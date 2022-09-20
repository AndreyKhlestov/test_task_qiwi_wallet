from loader import dp
from log.loger import logger
from states.user_states import UserState
from aiogram.types import Message, CallbackQuery
from utils.check_num import check_num
from utils.check_pay import check_pay
from loader import p2p
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext


# Получать сумму от пользователя и создавать киви счёт с полученной суммой (live_time 5 минут)
# Две кнопки прикрутить к сообщению об успешном создании платежа:
# Одна кнопка является ссылкой на оплату счета
# Вторая кнопка проверяет, прошёл ли платеж, если да - записывать сумму в баланс пользователя в боте, если нет -
# писать, что платеж не прошёл

@dp.message_handler(state=UserState.refill)
async def refill_num_money(message: Message, state: FSMContext):
    check = check_num(message.text)
    if isinstance(check, float):
        num_money = check
        logger.info(f'Пользователь {message.from_user.full_name} ввел сумму {num_money} руб. для пополнения')

        new_bill = await p2p.bill(amount=num_money, lifetime=5)
        await state.update_data(bill_id=new_bill.bill_id)

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
    if status == 'PAID':
        await call.message.edit_text('Оплата прошла успешно')
        await UserState.next()
    else:
        await call.message.edit_text('Платеж не прошёл')
