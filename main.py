from aiogram.utils import executor
from loader import dp
import handlers
from utils.set_bot_commands import set_default_commands


if __name__ == '__main__':
    # запуск режима длительного опроса
    executor.start_polling(dp, on_startup=set_default_commands, skip_updates=True)

