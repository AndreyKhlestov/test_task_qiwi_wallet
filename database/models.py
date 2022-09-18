# from peewee import *
#
# db = SqliteDatabase('database/database.db')
#
#
# class BaseModel(Model):
#     """Родительский класс"""
#     class Meta:
#         database = db
#
#
# class HealthDirection(BaseModel):
#     """Класс для работы с базой данных, содержащей название направлений вопросов
#     id - индивидуальный номер направления
#     direction - название направления"""
#
#     id = PrimaryKeyField(unique=True)
#     direction = CharField()
#
#
# class Categories(BaseModel):
#     """Класс для работы с базой данных, содержащей категории вопросов
#     id - индивидуальный номер категории
#     id_direction - id направления
#     category - название категории"""
#
#     id = PrimaryKeyField(unique=True)
#     id_direction = ForeignKeyField(HealthDirection)
#     category = CharField()
#
#
# class Questions(BaseModel):
#     """Класс для работы с базой данных, содержащей вопросы
#         id - индивидуальный номер вопроса
#         id_сategory - id категории
#         question - текст вопроса"""
#
#     id = PrimaryKeyField(unique=True)
#     id_category = ForeignKeyField(Categories)
#     question = CharField()
#
#
# class Answers(BaseModel):
#     """Класс для работы с базой данных, содержащий тексты заключений при определенном количестве ответов ДА
#         id - индивидуальный номер ответа
#         id_сategory - id категории
#         num_yes - количество ответов ДА
#         answer - текст заключения"""
#
#     id = PrimaryKeyField(unique=True)
#     id_category = ForeignKeyField(Categories)
#     num_yes = IntegerField()
#     answer = CharField()
