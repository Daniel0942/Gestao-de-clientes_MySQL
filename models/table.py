import os
from dotenv import  load_dotenv
from peewee import MySQLDatabase, Model, CharField, DateTimeField
import datetime

load_dotenv()
db = MySQLDatabase(
    host = os.getenv("host"),
    user = os.getenv("user"),
    password = os.getenv("password"),
    database = os.getenv("database"),
    port = int(os.getenv("port"))
)

class Cliente(Model):
    Nome = CharField()
    Email = CharField()
    data_registro = DateTimeField(default=datetime.datetime.now())

    class Meta:
        database = db