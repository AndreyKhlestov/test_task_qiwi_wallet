import os
from dotenv import load_dotenv, find_dotenv
from database.models import Users


if not find_dotenv():
    from my_logger.loger import logger
    logger.error('Переменные окружения не загружены т.к отсутствует файл .env')
    exit()

else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
QIWI_PRIV_KEY = os.getenv('QIWI_PRIV_KEY')

id_admin = 465654693

lifetime = 5

names_levels_log = ['debug', 'info', 'warning', 'error', 'critical']

# banned_users = set()
# all_block_users = Users.select().where(Users.block == True)
# for i_user in all_block_users:
#     banned_users.add(i_user.user_id)
