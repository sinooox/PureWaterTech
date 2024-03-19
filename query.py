import sqlite3
from config import DB_NAME


def insert(data):
    try:
        sqlite_connection = sqlite3.connect(DB_NAME)
        cursor = sqlite_connection.cursor()
        print("INS: Подключен к БД")
        sqlite_insert_query = data
        cursor.execute(sqlite_insert_query)
        sqlite_connection.commit()
        print(f"Запись успешно вставлена ​​в таблицу {DB_NAME}")
        cursor.close()
        return cursor.lastrowid
    except sqlite3.Error as error:
        print("INS: Ошибка при работе с БД", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("INS: Соединение с БД закрыто")


def delete(id):
    try:
        sqlite_connection = sqlite3.connect(DB_NAME)
        cursor = sqlite_connection.cursor()
        print("DEL: Подключен к БД")
        sqlite_delete_query = f"""DELETE FROM contacts WHERE id='{id}'"""
        cursor.execute(sqlite_delete_query)
        sqlite_connection.commit()
        print(f"Запись удалена из таблицы {DB_NAME}")
        cursor.close()
        return cursor.lastrowid
    except sqlite3.Error as error:
        print("DEL: Ошибка при работе с БД", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("DEL: Соединение с БД закрыто")


def out(data):
    try:
        sqlite_connection = sqlite3.connect(DB_NAME)
        cursor = sqlite_connection.cursor()
        print("OUT: Подключен к БД")
        sqlite_select_query = data
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


def out_all_id():
    try:
        sqlite_connection = sqlite3.connect(DB_NAME)
        cursor = sqlite_connection.cursor()
        print("OUT: Подключен к БД")
        sqlite_select_query = """SELECT id FROM contacts"""
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


def out_all_open():
    try:
        sqlite_connection = sqlite3.connect(DB_NAME)
        cursor = sqlite_connection.cursor()
        print("OUT: Подключен к БД")
        sqlite_select_query = """SELECT id FROM contacts WHERE status='Open'"""
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
        sqlite_connection = sqlite3.connect(DB_NAME)
        cursor = sqlite_connection.cursor()
        print("OUT: Подключен к БД")
        sqlite_select_query = """SELECT id FROM tg_authorized"""
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
        sqlite_connection = sqlite3.connect(DB_NAME)
        cursor = sqlite_connection.cursor()
        print("AUTH: Подключен к БД")
        sqlite_select_query = """SELECT id FROM tg_authorized"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()
        for i in records:
            if i[0] == id:
                return True
    except sqlite3.Error as error:
        print("AUTH: Ошибка при работе с БД", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("AUTH: Соединение с БД закрыто")
