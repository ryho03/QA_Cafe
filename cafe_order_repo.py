# The DB file contains the processes and functions to create our Database or connect to it as well as run the initial
# SQL
# The DB file should also contain query functions that the Service file can use to read or modify the data
import sqlite3


def setupConn(qacafedb_db):
    conn = sqlite3.connect(qacafedb_db)
    conn.execute("PRAGMA foreign_keys = 1")
    return conn


def createTable(qacafedb_db):
    sql_file = open("qacafe.sql")
    sql_string = sql_file.read()
    cursor = setupConn(qacafedb_db).cursor()
    cursor.executescript(sql_string)


def insertDrinksMenu():
    newDrink_name = input("Please enter new drink: ")
    newDrink_size = input("Please enter a size for pricing (SMA, MED, LAR): ")
    newDrink_price = float(input("Please enter a price: "))
    drink_query = f"INSERT INTO drink_menu (drink_name, drink_price, drink_size) VALUES ('{newDrink_name}', '{newDrink_price}', '{newDrink_size}');"
    cursor.execute(drink_query)
    return True


class Order:
    def __init__(self, drink_name, customer, size, quantity):
        self.drink_name = drink_name
        self.customer = customer
        self.size = size
        self.quantity = quantity

