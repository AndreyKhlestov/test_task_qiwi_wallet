from aiogram.utils import executor
from loader import dp
from my_logger.loger import logger
import handlers


if __name__ == '__main__':
    logger.info('Запуск бота')

    # запуск режима длительного опроса
    executor.start_polling(dp)
    # executor.start_polling(dp, skip_updates=True)

