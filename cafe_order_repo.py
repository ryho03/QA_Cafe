# The DB file contains the processes and functions to create our Database or connect to it as well as run the initial
# SQL
# The DB file should also contain query functions that the Service file can use to read or modify the data
import sqlite3


def setupConn(qacafedb_db):
    conn = sqlite3.connect(qacafedb_db)
    conn.execute("PRAGMA foreign_keys = 1")
    return conn


def createTable(self, qacafedb_db):
    sql_file = open("qacafe.sql")
    sql_string = sql_file.read()
    cursor = setupConn(qacafedb_db).cursor()
    cursor.executescript(sql_string)


class Order:
    def __init__(self, drink_name, customer, size, quantity):
        self.drink_name = drink_name
        self.customer = customer
        self.size = size
        self.quantity = quantity


class Drinks:
    def __init__(self, n_drink_name, n_drink_size, n_drink_price):
        self.nDrinkName = n_drink_name
        self.nDrinkSize = n_drink_size
        self.nDrinkPrice = n_drink_price
