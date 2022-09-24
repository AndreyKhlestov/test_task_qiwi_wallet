from aiogram.dispatcher.filters.state import StatesGroup, State


class UserState(StatesGroup):  # состояния пользователя
    ban = State()

    start = State()

    admin_menu = State()
    edit_balance = State()
    input_edit_balance = State()
    block_user = State()

    main_menu = State()
    refill = State()
    wait_pay = State()
    finish = State()

