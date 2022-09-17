from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config import BOT_TOKEN
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
# from database.models import db
# from database.models import db, HealthDirection, Categories, Questions, Answers

# соединение с базой данных
# with db:
#     db.create_tables([HealthDirection, Categories, Questions, Answers])
# db.connect()

# присвоение токена
bot = Bot(token=BOT_TOKEN)

# инициализируем обработчик входящих обновлений
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)
dp = Dispatcher(bot)

