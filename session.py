from sys import exit

from main import db, User, Post
from message import *
from utils import get_char




def begin_button():
    print(message2)
    # a = input('\tEnter your option: ')
    a = get_char()
    model_menu[a]()


def get(model, *args, **kwargs):
    print(get_message)
    a = get_char()
    instance = model.select().where(model.id==a).get()
    print(instance.id, instance.first_name, instance.last_name, instance.age, instance.created_at, status_code=200)

def get_all():
    all_users = User.select()
    response = '\n\n\tid\t\tfirst_name\tlast_name\n'
    for user in all_users:
        response += f'\t{user.id}\t\t{user.first_name}\t\t{user.last_name}\n'
    print(response)

def delete(model, *args, **kwargs):
    print(delete_message)
    a = int(get_char())
    model.delete().where(model.id==a).execute()
    # User.delete().where(User.id==a).execute()
    print(f'Object {a} succesfully deleted')
    # Post.delete().where(Post.id==a)

def create(*args, **kwargs):
    first_name = input('\tEnter first_name:')
    last_name = input('\tEnter last_name')
    age = int(input('\tEnter age'))
    User.create(first_name=first_name, last_name=last_name, age=age)
    print('\tUser created successfully!\n\n\n')

def update(*args, **kwargs):
    print(update_message)
    a = get_char()
    first_name = input('\tEnter first_name:')
    last_name = input('\tEnter last_name')
    age = int(input('\tEnter age'))
    User.update({
        'first_name': first_name,
        'last_name': last_name,
        'age': age
    }).where(User.id==a).execute()



user_options = {
    '1': get,
    '2': update,
    '3': delete,
    '4': create,
    '5': None,
    '6': exit
}

def user_button():
    get_all()
    print(model_options_message)
    a = get_char()
    if a == None:
        return    
    user_options[a](User) # delete(User)
    user_button()
    


def post_button():
    pass


model_menu = {
    '1': user_button,
    '2': post_button
}

welcome_menu = {
    '1': begin_button,
    '2': exit,
}



while True:
    print(message1)
    a = get_char()
    welcome_menu[a]()


'''
CRUD

~CREATE~(POST)
Создание объекта
Model.create(field1=value1, field2=value2)


~READ~(GET)
Получение сырого списка объектов
Model.select()

Получение одного объекта
Model.select().where(Model.id==id).get()


~UPDATE~(PUT, PATCH)
Изменение объекта
Model.update({field1: new_value1, field2: new_value2}).where(Model.id==id).execute()


~DELETE~(DELETE)
Удаление объекта
Model.delete().where(Model.field==value).execute()



'''
