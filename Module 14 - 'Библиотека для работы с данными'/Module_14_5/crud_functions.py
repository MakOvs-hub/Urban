'''


Изменения в Telegram-бот:
Кнопки главного меню дополните кнопкой "Регистрация".
Напишите новый класс состояний RegistrationState с следующими объектами класса State: username, email, age, balance(по умолчанию 1000).
Создайте цепочку изменений состояний RegistrationState.
Фукнции цепочки состояний RegistrationState:
sing_up(message):
Оберните её в message_handler, который реагирует на текстовое сообщение 'Регистрация'.
Эта функция должна выводить в Telegram-бот сообщение "Введите имя пользователя (только латинский алфавит):".
После ожидать ввода возраста в атрибут RegistrationState.username при помощи метода set.
set_username(message, state):
Оберните её в message_handler, который реагирует на состояние RegistrationState.username.
Если пользователя message.text ещё нет в таблице, то должны обновляться данные в состоянии username на message.text. Далее выводится сообщение "Введите свой email:" и принимается новое состояние RegistrationState.email.
Если пользователь с таким message.text есть в таблице, то выводить "Пользователь существует, введите другое имя" и запрашивать новое состояние для RegistrationState.username.
set_email(message, state):
Оберните её в message_handler, который реагирует на состояние RegistrationState.email.
Эта функция должна обновляться данные в состоянии RegistrationState.email на message.text.
Далее выводить сообщение "Введите свой возраст:":
После ожидать ввода возраста в атрибут RegistrationState.age.
set_age(message, state):
Оберните её в message_handler, который реагирует на состояние RegistrationState.age.
Эта функция должна обновляться данные в состоянии RegistrationState.age на message.text.
Далее брать все данные (username, email и age) из состояния и записывать в таблицу Users при помощи ранее написанной crud-функции add_user.
В конце завершать приём состояний при помощи метода finish().
'''



import sqlite3

connection = sqlite3.connect('data_mod_14_5.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    price TEXT NOT NULL
    )
    ''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOT NULL
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

def add_product(title, description, price):
    cursor.execute("INSERT INTO Products(title, description, price) VALUES(?,?,?)", (title, description, price))
    connection.commit()

def add_user(username, email, age, balance):
    cursor.execute("INSERT INTO Users(username, email, age, balance) VALUES(?,?,?,?)", (username, email, age, balance))
    connection.commit()

def is_included(username):
    check_user = cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    return check_user.fetchone()


# initiate_db()
# for i in range(1,5):
#     add_product(f'Product{i}', f'Описание{i}', f'{i * 100}')
# print(get_all_products())
