import csv
from connect import connect


# CREATE TABLE
def create_table():
    conn = connect()
    if conn is None:
        return

    cur = conn.cursor()

    try:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
                id SERIAL PRIMARY KEY,
                username VARCHAR(100) NOT NULL,
                phone VARCHAR(20) NOT NULL UNIQUE
            );
        """)
        conn.commit()
        print("Table created.")
    except Exception as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


# INSERT FROM CONSOLE
def insert_from_console():
    username = input("Enter username: ")
    phone = input("Enter phone: ")

    conn = connect()
    if conn is None:
        return

    cur = conn.cursor()

    try:
        cur.execute("""
            INSERT INTO phonebook (username, phone)
            VALUES (%s, %s)
        """, (username, phone))
        conn.commit()
        print("Inserted.")
    except Exception as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


# INSERT FROM CSV
def insert_from_csv(filename):
    conn = connect()
    if conn is None:
        return

    cur = conn.cursor()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)  # skip header

            for row in reader:
                cur.execute("""
                    INSERT INTO phonebook (username, phone)
                    VALUES (%s, %s)
                    ON CONFLICT (phone) DO NOTHING
                """, (row[0], row[1]))

        conn.commit()
        print("CSV inserted.")
    except Exception as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


# UPDATE CONTACT
def update_contact():
    username = input("Enter username: ")
    print("1 - Change name")
    print("2 - Change phone")
    choice = input("Choice: ")

    conn = connect()
    if conn is None:
        return

    cur = conn.cursor()

    try:
        if choice == "1":
            new_name = input("New name: ")
            cur.execute("""
                UPDATE phonebook
                SET username = %s
                WHERE username = %s
            """, (new_name, username))

        elif choice == "2":
            new_phone = input("New phone: ")
            cur.execute("""
                UPDATE phonebook
                SET phone = %s
                WHERE username = %s
            """, (new_phone, username))

        else:
            print("Invalid choice.")
            return

        conn.commit()
        print("Updated.")
    except Exception as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


# SHOW ALL CONTACTS
def show_all():
    conn = connect()
    if conn is None:
        return

    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM phonebook")
        rows = cur.fetchall()

        if not rows:
            print("PhoneBook is empty.")
        else:
            for row in rows:
                print(row)
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


# SEARCH BY NAME
def search_by_name():
    name = input("Enter name: ")

    conn = connect()
    if conn is None:
        return

    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT * FROM phonebook
            WHERE username ILIKE %s
        """, ('%' + name + '%',))

        rows = cur.fetchall()
        if not rows:
            print("No contacts found.")
        else:
            for row in rows:
                print(row)
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


# SEARCH BY PHONE PREFIX
def search_by_prefix():
    prefix = input("Enter prefix: ")

    conn = connect()
    if conn is None:
        return

    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT * FROM phonebook
            WHERE phone LIKE %s
        """, (prefix + '%',))

        rows = cur.fetchall()
        if not rows:
            print("No contacts found.")
        else:
            for row in rows:
                print(row)
    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


# DELETE CONTACT
def delete_contact():
    print("1 - Delete by username")
    print("2 - Delete by phone")
    choice = input("Choice: ")

    conn = connect()
    if conn is None:
        return

    cur = conn.cursor()

    try:
        if choice == "1":
            username = input("Enter username: ")
            cur.execute("DELETE FROM phonebook WHERE username = %s", (username,))
        elif choice == "2":
            phone = input("Enter phone: ")
            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
        else:
            print("Invalid choice.")
            return

        conn.commit()
        print("Deleted.")
    except Exception as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


# MENU
def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Create table")
        print("2 - Insert (console)")
        print("3 - Insert (CSV)")
        print("4 - Update")
        print("5 - Show all")
        print("6 - Search by name")
        print("7 - Search by prefix")
        print("8 - Delete")
        print("0 - Exit")

        choice = input(">>> ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            file = input("CSV filename: ")
            insert_from_csv(file)
        elif choice == "4":
            update_contact()
        elif choice == "5":
            show_all()
        elif choice == "6":
            search_by_name()
        elif choice == "7":
            search_by_prefix()
        elif choice == "8":
            delete_contact()
        elif choice == "0":
            break
        else:
            print("Invalid")


if __name__ == "__main__":
    menu()
