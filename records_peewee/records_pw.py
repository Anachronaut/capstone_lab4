from peewee import *

db = SqliteDatabase('test_records.sqlite')

class Record_Holder(Model):
    name = CharField()
    country = CharField()
    total_catches = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'{self.name} is from {self.country} and has {self.total_catches} catches'

db.connect()
db.create_tables([Record_Holder])

def print_table(): #prints full record_holder table in descending order by total_catches
    record_holders = (Record_Holder.select()).order_by(Record_Holder.total_catches.desc())
    print()
    print('Record Holders for Most Catches')
    print("-"*33)
    for holder in record_holders:
        print(holder)
    print()

def update_catches(holder_name, new_catches): #updates total_catches for Record_Holder object by name in record_holder table
    Record_Holder.update(total_catches = new_catches).where(Record_Holder.name == holder_name).execute()
    print_table()

def delete_holder(holder_name): #deletes Record_Holder object by name from record_holder table
    Record_Holder.delete().where(Record_Holder.name == holder_name).execute()
    print_table()

def add_holder(holder_name,holder_country,holder_catches): #adds new Record_Holder object to record_holder table
     new_holder = Record_Holder(name = holder_name, country = holder_country, total_catches = holder_catches)
     new_holder.save()
     print_table()

def search_holder(holder_name): #displays one Record_Holder object by name from record_holders table
    holder = Record_Holder.get_or_none(Record_Holder.name == holder_name)
    print()
    print(holder)
    print()


def main():
    while True: #display menu
        print()
        print('(1): Add a new record holder')
        print('(2): Search for a record holder')
        print('(3): Update number of catches for a record holder')
        print('(4): Delete a record holder')
        print()

        choice = input('Please choose Option 1, 2, 3, 4 [Enter "Q" to quit]: ')

        if choice == "1":   #Add record holder to table
            name = str(input("Enter record holder's name: "))
            country = str(input("Enter the country "+name+" is from: "))
            catches = int(input("Enter the number of catches "+name+" has: "))
            add_holder(name,country,catches)
        elif choice == "2": #Search for record holder by name
            name = str(input("Enter record holder's name: "))
            search_holder(name)
        elif choice == "3": #Update catches for record holder by name
            name = str(input("Enter record holder's name: "))
            new_catches = int(input("Enter new total number of catches: "))
            update_catches(name,new_catches)
        elif choice == "4": #Delete record holder by name
            name = str(input("Enter record holder's name: "))
            delete_holder(name)
        elif choice == "Q" or choice == "q":
            quit()
        else:
            print("Invalid entry")

main()
