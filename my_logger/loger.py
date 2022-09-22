import logging
from my_logger.get_log_file_handler import get_log_file_handler
from my_logger.get_stream_handler import get_stream_handler
from config import names_levels_log


def get_logger() -> logging.Logger:
    """Регистратор"""
    my_logger = logging.getLogger('logger')
    my_logger.setLevel(logging.DEBUG)

    # Создание форматера
    log_format = '%(asctime)s - [%(levelname)s] - %(filename)s (%(funcName)s: line %(lineno)d) - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(fmt=log_format, datefmt=date_format)

    # добавление настроенных обработчиков в логгер
    for level in names_levels_log:
        my_logger.addHandler(get_log_file_handler(formatter, level))
    my_logger.addHandler(get_stream_handler(formatter))
    return my_logger


logger = get_logger()
