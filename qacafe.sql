CREATE TABLE cust_orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cust_name VARCHAR(30),
    drink_choice INTEGER,
    drink_size VARCHAR(3),
    extras INTEGER
    order_price FLOAT
);

CREATE TABLE drink_menu (
    drink_id INTEGER PRIMARY KEY AUTOINCREMENT,
    drink_price FLOAT,

    FOREIGN KEY(drink_price) REFERENCES price_list(drink_price)
);


CREATE TABLE price_list (
    price_id INTEGER PRIMARY KEY AUTOINCREMENT,
    drink_price FLOAT,





);