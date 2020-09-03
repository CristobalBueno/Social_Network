import sqlite3
from sqlite3 import Error
import pickle
"""
import pickle
listaSerializada = pickle.dumps([1,2,3,4])
print(listaSerializada)

Y con aquel dato lo que harias es almacenarlo en alguna columna tipo BLOB

Luego cuando quieras obtener el valor a partir de la consulta a tu BD, usarias el metodo loads()

listaSerializada = pickle.dumps([1,2,3,4])
listaNoSerializada = pickle.loads(listaSerializada)
print('Lista %s' % listaNoSerializada)
"""
# https://pynative.com/python-sqlite-blob-insert-and-retrieve-digital-data/

def create_connection(path):
    global BDD_Connection

    try:
        BDD_Connection = sqlite3.connect(path)
        print("BDD -> The connection has been established")
    except Error as e:
        print(f"Exception create_connection: {e.args}")

    return BDD_Connection


def execute_query(query):
    global cursor
    cursor = BDD_Connection.cursor()
    try:
        cursor.execute(query)
        BDD_Connection.commit()
        print("BDD -> The query has been made")
        return True
    except Error as e:
        print(f"Exception execute_query: {e.args}")
        return False


def show_bdd(query):
    try:
        dates = cursor.execute(query).fetchall()
        print(f"Show all dates: {dates}")
        return dates
    except Error as e:
        print(f"Exception show_bdd: {e.args}")


