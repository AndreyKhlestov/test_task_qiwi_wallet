from loader import dp
from my_logger.loger import logger
from states.user_states import UserState
from aiogram.types import Message
from handlers.main_menu import main_menu
from config import id_admin
from handlers.admin_menu.admin_menu import start_admin_menu
from database.models import Users

user_id = 465654693
balanse = Users.select().where(Users.user_id == user_id).get().balance
Users.update(balance=balanse + 5.2).where(Users.user_id == user_id).execute()
# user_info = Users.create(user_id=user_id, user_name=user_name, balance=0, block=False)
# HotelRequest.update(main_info=text_main_info).where(HotelRequest.id == request_id).execute()
