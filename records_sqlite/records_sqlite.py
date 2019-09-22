import sqlite3

db_url = 'test_records.db'

def print_table():  #prints full RECORDS table, sorted by Catches in descending order
    with sqlite3.connect(db_url) as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM RECORDS ORDER BY total_catches DESC')
        table_rows = cur.fetchall()
        print()
        print("(Record Holder, Country, Catches)")
        print("-"*33)
        for row in table_rows:
            print(row)
        print()
    conn.close()

def delete_holder(name):    #delete a record holder from RECORDS table
    name = name.upper()
    with sqlite3.connect(db_url) as conn:
        conn.execute('DELETE FROM RECORDS WHERE name = ?', (name, ))
    conn.close()
    print_table()

def update_catches(name, new_catches):  #updates total number of catches a record holder has in RECORDS table
    name = name.upper()
    with sqlite3.connect(db_url) as conn:
        conn.execute('UPDATE RECORDS SET total_catches = ? WHERE name = ?', (new_catches, name))
    conn.close()
    print_table()

def search_holder(name):    #search for a record holder in RECORDS table by name
    name = name.upper()
    with sqlite3.connect(db_url) as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM RECORDS WHERE name = ?', (name, ))
        print()
        print(cur.fetchall())
        print()
    conn.close()

def add_holder(name,country,catches): #add a new record holder to RECORDS table
    name = name.upper()
    with sqlite3.connect(db_url) as conn:
        conn.execute('INSERT INTO RECORDS VALUES (?,?,?)', (name, country, catches))
    conn.close()
    print_table()

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
