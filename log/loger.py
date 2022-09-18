import logging


log_format = '%(asctime)s - [%(levelname)s] - %(filename)s (%(funcName)s: line %(lineno)d) - %(message)s'
date_format = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter(fmt=log_format, datefmt=date_format)


def get_file_handler_error():
    """Файловый обработчик только для ошибок и предупреждений"""
    file_handler_error = logging.FileHandler('errors_log.log')
    file_handler_error.setLevel(logging.WARNING)
    file_handler_error.setFormatter(formatter)
    return file_handler_error


def get_file_handler_all():
    """Файловый обработчик для всех сообщений"""
    file_handler_all = logging.FileHandler('all_log.log')
    file_handler_all.setLevel(logging.DEBUG)
    file_handler_all.setFormatter(formatter)
    return file_handler_all


def get_stream_handler():
    """Консольный обработчик"""
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    return stream_handler


def get_logger():
    """Регистратор"""
    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler_all())
    logger.addHandler(get_file_handler_error())
    logger.addHandler(get_stream_handler())
    return logger


logger = get_logger()
# logger.debug('debug')
# logger.info('Info')
# logger.warning('warning')
# logger.error('error')
# logger.critical('critical')

# logging.basicConfig(
#     level=logging.WARNING,
#     filename='errors_log.log',
#     format='%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s',
#     datefmt='%H:%M:%S',
#     )
