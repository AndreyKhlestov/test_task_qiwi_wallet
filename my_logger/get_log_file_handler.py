import logging
from my_logger.filter import Filter


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
    file_handler = logging.FileHandler(f'my_logger/logs/{level}.log')
    file_handler.setLevel(level_log[level])
    file_handler.setFormatter(formatter)
    file_handler.addFilter(Filter(level_log[level]))
    return file_handler
