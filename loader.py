from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from config import BOT_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import QIWI_PRIV_KEY
from pyqiwip2p import AioQiwiP2P
from database.models import db, Users


# соединение с базой данных
with db:
    db.create_tables([Users])

# присвоение токена
bot = Bot(token=BOT_TOKEN)

# инициализируем обработчик входящих обновлений
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

p2p = AioQiwiP2P(auth_key=QIWI_PRIV_KEY)


