import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    from my_logger.loger import logger
    logger.error('Переменные окружения не загружены т.к отсутствует файл .env')
    exit()
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
QIWI_PRIV_KEY = os.getenv('QIWI_PRIV_KEY')

id_admin = 465654693

lifetime = 1

names_levels_log = ['debug', 'info', 'warning', 'error', 'critical']
