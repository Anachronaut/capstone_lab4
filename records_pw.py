from peewee import *

db = SqliteDatabase('records.sqlite')

class Record_Holder(Model):
    name = CharField()
    country = CharField()
    catches = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.name} is from {self.country} and has {self.catches} catches'

main():
    
