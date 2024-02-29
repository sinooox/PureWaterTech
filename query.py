import sqlite3


db_name = 'contacts.db'


def insert(data):
    try:
        sqlite_connection = sqlite3.connect(db_name)
        cursor = sqlite_connection.cursor()
        print("INS: Подключен к БД")
        sqlite_insert_query = data
        cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        print(f"Запись успешно вставлена ​​в таблицу {db_name} ", cursor.rowcount)
        cursor.close()

    except sqlite3.Error as error:
        print("INS: Ошибка при работе с БД", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("INS: Соединение с БД закрыто")


def out(query):
    try:
        sqlite_connection = sqlite3.connect(db_name)
        cursor = sqlite_connection.cursor()
        print("OUT: Подключен к БД")
        sqlite_select_query = query
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()
        return records

    except sqlite3.Error as error:
        print("OUT: Ошибка при работе с БД", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("OUT: Соединение с БД закрыто")


def out_all_contacts():
    try:
        sqlite_connection = sqlite3.connect(db_name)
        cursor = sqlite_connection.cursor()
        print("OUT: Подключен к БД")
        sqlite_select_query = """SELECT * from contacts"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()
        return records

    except sqlite3.Error as error:
        print("OUT: Ошибка при работе с БД", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("OUT: Соединение с БД закрыто")


def get_ids():
    try:
        sqlite_connection = sqlite3.connect(db_name)
        cursor = sqlite_connection.cursor()
        print("OUT: Подключен к БД")
        sqlite_select_query = """SELECT id from tg_authorized"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()
        return records

    except sqlite3.Error as error:
        print("OUT: Ошибка при работе с БД", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("OUT: Соединение с БД закрыто")


def auth(id):
    try:
        sqlite_connection = sqlite3.connect(db_name)
        cursor = sqlite_connection.cursor()
        print("OUT: Подключен к БД")
        sqlite_select_query = """SELECT id from tg_authorized"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        cursor.close()

        for i in records:
            if i[0] == id:
                return True

    except sqlite3.Error as error:
        print("OUT: Ошибка при работе с БД", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("OUT: Соединение с БД закрыто")