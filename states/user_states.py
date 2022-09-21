from aiogram.dispatcher.filters.state import StatesGroup, State


class UserState(StatesGroup):  # состояния пользователя
    start = State()
    main_menu = State()
    refill = State()
    wait_pay = State()
    finish = State()
