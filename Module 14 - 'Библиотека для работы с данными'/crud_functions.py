'''
Цель: написать простейшие CRUD функции для взаимодействия с базой данных.

Задача "Продуктовая база":
Подготовка:
Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его, следуя пунктам задачи ниже.

Дополните ранее написанный код для Telegram-бота:
Создайте файл crud_functions.py и напишите там следующие функции:
initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса. Эта таблица должна содержать следующие поля:
id - целое число, первичный ключ
title(название продукта) - текст (не пустой)
description(описание) - текст
price(цена) - целое число (не пустой)
get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.

Изменения в Telegram-бот:
В самом начале запускайте ранее написанную функцию get_all_products.
Измените функцию get_buying_list в модуле с Telegram-ботом, используя вместо обычной нумерации продуктов функцию get_all_products. Полученные записи используйте в выводимой надписи: "Название: <title> | Описание: <description> | Цена: <price>"
Перед запуском бота пополните вашу таблицу Products 4 или более записями для последующего вывода в чате Telegram-бота.

'''



import sqlite3

connection = sqlite3.connect('data_mod_14_4.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price TEXT NOT NULL
    )
    ''')
    connection.commit()

def get_all_products():
    all_values = cursor.execute("SELECT * FROM Products").fetchall()
    # list_values = ''
    # for value in all_values:
    #     list_values += f'{value[0]}|{value[1]}|{value[2]}|{value[3]}\n'
    # connection.commit()
    return all_values

def add_product(id, title, description, price):
    cursor.execute("INSERT INTO Products VALUES(?,?,?,?)", (id,title, description, price))
    connection.commit()


# initiate_db()
# for i in range(1,5):
#     add_product(f'{i}',f'Product{i}', f'Описание{i}', f'{i * 100}')
# print(get_all_products())