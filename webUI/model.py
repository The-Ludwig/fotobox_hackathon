from peewee import SqliteDatabase, Model, DateTimeField, IntegerField, CharField

db = SqliteDatabase("image.sqlite")


class Image(Model):
    datetime = DateTimeField()
    loc = CharField()

    class Meta:
        database = db
