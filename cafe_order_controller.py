# Controller acts as the API for the app, for now, it will exist as a terminal based app.
# It will run commands from the service file, which in turn uses the DB file to
# query and create data and will return the data back to the user

from cafe_order_service import *


def runApp():
    print(
        """
        Welcome to the QA Cafe!
        What would you like to do today?    
        
        1. Create an order
        2. View an order (NOT IN USE)
        3. View all orders (NOT IN USE)
        4. Update an existing order (NOT IN USE)
        5. Delete an order (NOT IN USE)
        6. Delete all orders (NOT IN USE)
        7. Update drinks menu
        8. Update price list (NOT IN USE)
        """
    )
    appRun = True

    while appRun:
        choice = int(input("Please choose an option from the menu: "))
        if choice == 1:
            create_order(drink_name="", customer="", size="", quantity=0)
        if choice == 7:
            insertDrinksMenu()
        reorder_drink = int(input("Would you like to order another drink? 1. Yes (NOT IN USE) 2. No: "))
        if reorder_drink == 2:
            appRun = False
        return appRun


runApp()
