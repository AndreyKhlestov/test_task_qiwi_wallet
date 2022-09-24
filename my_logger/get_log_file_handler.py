import logging
from my_logger.filter import Filter
from logging.handlers import RotatingFileHandler


level_log = {
    'debug': 10,
    'info': 20,
    'warning': 30,
    'error': 40,
    'critical': 50
}


def get_log_file_handler(formatter: logging.Formatter, level: str) -> logging.FileHandler:
    """Функция для созданий файлового обработчика.
    Получает готовый форматер и уровень логирования"""
    file_handler = RotatingFileHandler(f'my_logger/logs/{level}.log', maxBytes=5*1024*1024, backupCount=3)
    file_handler.setLevel(level_log[level])
    file_handler.setFormatter(formatter)
    file_handler.addFilter(Filter(level_log[level]))
    return file_handler
