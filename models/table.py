from peewee import MySQLDatabase, Model, CharField, DateTimeField
import datetime

db = MySQLDatabase(
    host = "junction.proxy.rlwy.net",
    user = "root",
    password = "oWYRIWUcpsUqBqocUaPswbGEGxkGPEBo",
    database = "railway",
    port = 43858
)

class Cliente(Model):
    Nome = CharField()
    Email = CharField()
    data_registro = DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = db