from database.models import db, Users

with db:
    db.create_tables([Users])

request_id = Users.create(user_id=4547566, user_name='andrei', balance=125, block=False)

# all_users = Users.select()
# for user in all_users:
#     print(user.user_id, user.user_name, user.balance, user.block)

users = Users.select().where(Users.user_id == 454756)
if not users:
    print('None')
else:
    for user in users:
        print(user.user_id, user.user_name, user.balance, user.block)
    print('ok')
# bd_questions = Questions.select().where(Questions.id_category == data['id_category']).order_by(Questions.id)
# bd_categories = Categories.select().where(Categories.id_direction == id_direction)
