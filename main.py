import datetime

import peewee


db = peewee.SqliteDatabase('my_db.db')


class User(peewee.Model):
    first_name = peewee.CharField(max_length=255)
    last_name = peewee.CharField(max_length=255)

    age = peewee.IntegerField()

    created_at = peewee.DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = db


class Post(peewee.Model):
    title = peewee.CharField(max_length=255)
    text = peewee.TextField()

    author = peewee.ForeignKeyField(User, field='id')
    
    created_at = peewee.DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = db


db.connect()
# \c my_db

db.create_tables([User, Post])
# CREATE TABLE user;
# CREATE TABLE post;





