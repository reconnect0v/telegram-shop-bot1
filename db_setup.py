import sqlite3

# Создаем базу данных
conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

# Таблица товаров
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        description TEXT
    )''')
conn.commit()

# Пример заполнения товаров
products = [
    ('Товар 1', 1000, 'Описание товара 1'),
    ('Товар 2', 2000, 'Описание товара 2'),
    ('Товар 3', 1500, 'Описание товара 3'),
]
cursor.executemany("INSERT INTO products (name, price, description) VALUES (?, ?, ?)", products)
conn.commit()
conn.close()
