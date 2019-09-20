import sqlite3

db_url = 'test_records.db'

def delete_holder(name):
    with sqlite3.connect(db_url) as conn:
        conn.execute('DELETE FROM RECORDS WHERE name = ?', (name, ))
    conn.close()

def update_catches(name, new_catches):
    with sqlite3.connect(db_url) as conn:
        conn.execute('UPDATE RECORDS SET total_catches = ? WHERE name = ?', (new_catches, name))
    conn.close()

def search_holder(name):
    with sqlite3.connect(db_url) as conn:
        cur = conn.cursor()
        conn.execute('SELECT * FROM RECORDS WHERE name = ?', (name, ))
        print(cur.fetchall())
    conn.close()

def add_holder(name,country,catches):
    with sqlite3.connect(db_url) as conn:
        conn.execute('INSERT INTO RECORDS VALUES (?,?,?)', (name, country, catches))
    conn.close()

def main():
    while True:
        print('(1): Add a new record holder')
        print('(2): Search for a record holder')
        print('(3): Update number of catches for a record holder')
        print('(4): Delete a record holder')

        choice = input('Please choose Option 1, 2, 3, 4 [Enter "Q" to quit]: ')

        if choice == 1:
            name = str(input("Enter record holder's name: "))
            country = str(input("Enter the country "+name+" is from:"))
            catches = int(input("Enter the number of catches "+name+" has: "))
            add_holder(name,country,catches)
        elif choice == 2:
            name = str(input("Enter record holder's name: "))
            search_holder(name)
        elif choice == 3:
            name = str(input("Enter record holder's name: "))
            new_catches = int(input("Enter new total number of catches: "))
            update_catches(name,new_catches)
        elif choice == 4:
            name = str(input("Enter record holder's name: "))
            delete_holder(name)
        elif choice == "Q" or choice == "q":
            quit()
        else:
            print("Invalid entry")

main()
