from aiogram.utils import executor
from loader import dp
import handlers


if __name__ == '__main__':
    # запуск режима длительного опроса
    executor.start_polling(dp, skip_updates=True)

