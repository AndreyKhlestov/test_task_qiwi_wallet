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
    # data = (await state.get_data()).get('bill_id')
    print(message.from_user.id)




