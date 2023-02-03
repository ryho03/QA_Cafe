CREATE TABLE cust_orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cust_name VARCHAR(30),
    drink_choice INTEGER,
    drink_size CHAR(3),
    extras INTEGER,
    order_price FLOAT
    FOREIGN KEY(drink_size) REFERENCES drink_menu(drink_size)
);

CREATE TABLE drink_menu (
    drink_id INTEGER PRIMARY KEY AUTOINCREMENT,
    drink_name VARCHAR (20),
    drink_price FLOAT,
    drink_size CHAR(3)
);
