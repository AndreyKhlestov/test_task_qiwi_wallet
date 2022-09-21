import os
from dotenv import load_dotenv, find_dotenv
from log.loger import logger

if not find_dotenv():
    logger.error('Переменные окружения не загружены т.к отсутствует файл .env')
    exit()
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
QIWI_PRIV_KEY = os.getenv('QIWI_PRIV_KEY')
lifetime = 1
