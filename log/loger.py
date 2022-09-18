import logging
import sys


def get_file_handler_error(formatter: logging.Formatter) -> logging.FileHandler:
    """Файловый обработчик только для ошибок и предупреждений"""
    file_handler_error = logging.FileHandler('log/errors_log.log')
    file_handler_error.setLevel(logging.WARNING)
    file_handler_error.setFormatter(formatter)
    return file_handler_error


def get_file_handler_all(formatter: logging.Formatter) -> logging.FileHandler:
    """Файловый обработчик для всех сообщений"""
    file_handler_all = logging.FileHandler('log/all_log.log')
    file_handler_all.setLevel(logging.DEBUG)
    file_handler_all.setFormatter(formatter)
    return file_handler_all


def get_stream_handler(formatter: logging.Formatter) -> logging.StreamHandler:
    """Консольный обработчик"""
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    return stream_handler


def get_logger() -> logging.Logger:
    """Регистратор"""
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)

    # Создание форматера
    log_format = '%(asctime)s - [%(levelname)s] - %(filename)s (%(funcName)s: line %(lineno)d) - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(fmt=log_format, datefmt=date_format)

    # добавление настроенных обработчиков в логгер
    logger.addHandler(get_file_handler_all(formatter))
    logger.addHandler(get_file_handler_error(formatter))
    logger.addHandler(get_stream_handler(formatter))
    return logger


logger = get_logger()
