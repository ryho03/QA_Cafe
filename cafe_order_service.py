# The service file interacts with the DB file to Query or Modify data within the database
# Typically there will be a function for each process that is required, and these will take in data and return data
from cafe_order_repo import *


def __str__(self):
    return f"Drink: {self.drink_name} Customer Name:{self.customer} Size: {self.size} Quantity: {self.quantity}"


def create_order(drink_name, customer, size, quantity):
    print(
        """
        Welcome to the ordering screen!
        What may I get for you today?    

        1. Americano
        2. Cappuccino
        3. Latte
        4. Mocha
        5. Hot Chocolate
        6. Back
        """
    )
    c_o_run = True

    while c_o_run:
        choice = int(input("Please choose an option from the menu (using numbers): "))
        if choice == 1:
            drink_name = "Americano"
            c_o_run = False
        elif choice == 2:
            drink_name = "Cappuccino"
            c_o_run = False
        elif choice == 3:
            drink_name = "Latte"
            c_o_run = False
        elif choice == 4:
            drink_name = "Mocha"
            c_o_run = False
        elif choice == 5:
            drink_name = "Hot Chocolate"
            c_o_run = False
        elif choice == 6:
            c_o_run = False
            return
        else:
            print("The option you selected is invalid, please retry: ")
            d_o_run = False

    d_o_run = True

    while d_o_run:
        choice = int(input("What size drink would you like? 1.Small 2.Medium 3.Large:"))
        if choice == 1:
            size = "SMA"
            d_o_run = False
        elif choice == 2:
            size = "MED"
            d_o_run = False
        elif choice == 3:
            size = "LAR"
            d_o_run = False
        else:
            print("The option you selected is invalid, please retry: ")

    quantity = int(input("How many would you like? "))
    customer = input("What is your name? ")
    print(drink_name, customer, size, quantity)
    Order(drink_name=drink_name, customer=customer, size=size, quantity=quantity)
    # order = Order(drink_name, str(customer), size, quantity)
    print(Order)
    return Order


def insertDrinksMenu(self):
    newDrink_name = input("Please enter new drink: ")
    newDrink_size = input("Please enter a size for pricing (SMA, MED, LAR): ")
    newDrink_price = float(input("Please enter a price: "))
    drink_query = f"INSERT INTO drink_menu (drink_name, drink_price, drink_size) VALUES ('{newDrink_name}', '{newDrink_price}', '{newDrink_size}');"
    self.cursor.execute(drink_query)
    Drinks(n_drink_name=newDrink_name, n_drink_size=newDrink_size, n_drink_price=newDrink_price)
    return True
