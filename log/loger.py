import logging


# logging.basicConfig(
#     level=logging.WARNING,
#     filename='errors_log.log',
#     format='%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s',
#     datefmt='%H:%M:%S',
#     )

logging.basicConfig(
    format='%(asctime)s - [%(levelname)s] - %(filename)s (%(funcName)s: %(lineno)d) - %(message)s',
    )


logging.debug('debug')
logging.info('Info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')
