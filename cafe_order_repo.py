# The DB file contains the processes and functions to create our Database or connect to it as well as run the initial
# SQL
# The DB file should also contain query functions that the Service file can use to read or modify the data
# Order.py example is repo
# import sqlite3
#
#
# def setupConn(qacafedb_db):
#     conn = sqlite3.connect(qacafedb_db)
#     return conn


class Order:
    def __init__(self, drink_name, customer, size, quantity):
        self.drink_name = drink_name
        self.customer = customer
        self.size = size
        self.quantity = quantity
