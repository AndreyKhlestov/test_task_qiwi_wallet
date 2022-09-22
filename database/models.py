from peewee import *

db = SqliteDatabase('database/database.db')


class BaseModel(Model):
    """Родительский класс"""
    class Meta:
        database = db


class Users(BaseModel):
    """Класс для работы с базой данных, содержащей пользователей бота
    user_id - индивидуальный номер пользователя в Telegram
    user_name - имя пользователя
    balance - состояние баланса
    block - состояние пользователя (заблокирован - True, иначе - False)"""

    user_id = IntegerField()
    user_name = CharField()
    balance = FloatField()
    block = BooleanField()
