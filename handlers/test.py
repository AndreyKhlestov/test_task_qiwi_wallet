from loader import dp
from aiogram.types import Message
from keyboards.default_inline_keyboards import inline_keyboards
from loader import p2p
from pyqiwip2p.p2p_types.errors import QiwiError
from aiogram.dispatcher import FSMContext


# pyqiwip2p.p2p_types.errors.QiwiError: api.invoice.not.found - Счёт не найден
@dp.message_handler(commands=['test'])
async def welcome(message: Message, state: FSMContext):
    # await state.update_data(bill_id=12345)
    data = (await state.get_data()).get('bill_id')
    print(data)


    # try:
    #     check = await p2p.check(bill_id=1243)
    # except QiwiError:
    #     print('None')
    # print(await check_pay(1234))

    # bill_id = 'WhiteApfel-PyQiwiP2P-66885824-321'
    # new_bill = await p2p.bill(amount=228, lifetime=5)
    # print(new_bill.bill_id, new_bill.pay_url)
    bill_id = 1234
    # создание счета
    # new_bill = await p2p.bill(bill_id=1234, amount=60, lifetime=7)

    # отмена счета
    # await p2p.reject(bill_id=bil l_id)

    # Проверим статус выставленного счета
    # print((await p2p.check(bill_id=bill_id)).status)
    # status = await p2p.check(bill_id=bill_id)
    # print('ok')
    # Потеряли ссылку на оплату счета? Не проблема!
    # print((await p2p.check(bill_id=bill_id)).pay_url)





