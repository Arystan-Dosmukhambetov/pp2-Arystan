from connect import connect
# -----------------------------
# CREATE TABLE (optional)
# -----------------------------
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
        print("Table ready.")
    except Exception as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


# -----------------------------
# UPSERT (CALL PROCEDURE)
# -----------------------------
def upsert_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
        conn.commit()
        print("Saved (insert/update).")
    except Exception as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


# -----------------------------
# BULK INSERT (CALL PROCEDURE)
# -----------------------------
def bulk_insert():
    print("Enter names (comma separated):")
    names = input().split(",")

    print("Enter phones (comma separated):")
    phones = input().split(",")

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "CALL bulk_insert_contacts(%s, %s)",
            (names, phones)
        )
        conn.commit()
        print("Bulk insert done.")
    except Exception as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


# -----------------------------
# SEARCH (FUNCTION)
# -----------------------------
def search_contacts():
    pattern = input("Search pattern: ")

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "SELECT * FROM get_contacts_by_pattern(%s)",
            (pattern,)
        )

        rows = cur.fetchall()

        if not rows:
            print("No results.")
        else:
            for r in rows:
                print(r)

    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


# -----------------------------
# PAGINATION (FUNCTION)
# -----------------------------
def paginated():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute(
            "SELECT * FROM get_contacts_paginated(%s, %s)",
            (limit, offset)
        )

        rows = cur.fetchall()

        if not rows:
            print("Empty.")
        else:
            for r in rows:
                print(r)

    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


# -----------------------------
# DELETE (CALL PROCEDURE)
# -----------------------------
def delete_contact():
    value = input("Enter username or phone: ")

    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute("CALL delete_contact(%s)", (value,))
        conn.commit()
        print("Deleted.")
    except Exception as e:
        conn.rollback()
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


# -----------------------------
# SHOW ALL (simple SELECT)
# -----------------------------
def show_all():
    conn = connect()
    cur = conn.cursor()

    try:
        cur.execute("SELECT * FROM phonebook ORDER BY id")
        rows = cur.fetchall()

        for r in rows:
            print(r)

    except Exception as e:
        print("Error:", e)
    finally:
        cur.close()
        conn.close()


# -----------------------------
# MENU
# -----------------------------
def menu():
    while True:
        print("\n====== PHONEBOOK (PRACTICE 8) ======")
        print("1 - Create table")
        print("2 - Upsert contact")
        print("3 - Bulk insert")
        print("4 - Search contacts")
        print("5 - Paginated view")
        print("6 - Show all")
        print("7 - Delete contact")
        print("0 - Exit")

        choice = input(">>> ")

        if choice == "1":
            create_table()
        elif choice == "2":
            upsert_contact()
        elif choice == "3":
            bulk_insert()
        elif choice == "4":
            search_contacts()
        elif choice == "5":
            paginated()
        elif choice == "6":
            show_all()
        elif choice == "7":
            delete_contact()
        elif choice == "0":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
