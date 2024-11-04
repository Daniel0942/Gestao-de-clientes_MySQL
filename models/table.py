from peewee import SqliteDatabase, Model, CharField, DateTimeField
import datetime

db = SqliteDatabase('Custom_clientes.db')

class Cliente(Model):
    nome = CharField()
    email = DateTimeField()
    data_registro = DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = db