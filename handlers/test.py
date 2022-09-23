from loader import dp
from aiogram.types import Message
from keyboards.default_inline_keyboards import inline_keyboards
from loader import p2p
from pyqiwip2p.p2p_types.errors import QiwiError
from aiogram.dispatcher import FSMContext
from states.user_states import UserState


# pyqiwip2p.p2p_types.errors.QiwiError: api.invoice.not.found - Счёт не найден
@dp.message_handler(commands=['test'])
async def welcome(message: Message, state: FSMContext):
    # g = await dp.get_users("hankipoiii")
    # status = g.status
    # print(status)
    await UserState.start.set()
    state = await state.get_state()
    # state = dp.current_state(user=message.from_user.id)
    # await state.update_data(bill_id=12345)
    # data = (await state.get_data()).get('bill_id')
    print(state)
    # id = str(message.from_user.id)
    # state.storage['data'][id][id]['state']
    # await state.storage['data']




