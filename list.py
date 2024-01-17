from main import db, User, Post


all_users = User.select(User.id, User.first_name, User.last_name, User.age)
for user in all_users:
    print(user.id, user.first_name, user.last_name, user.age)
