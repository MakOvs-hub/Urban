import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

# Создайте файл базы данных not_telegram.db и подключитесь к ней, используя встроенную библиотеку sqlite3.
# Создайте объект курсора и выполните следующие действия при помощи SQL запросов:
# Создайте таблицу Users, если она ещё не создана. В этой таблице должны присутствовать следующие поля:
# id - целое число, первичный ключ
# username - текст (не пустой)
# email - текст (не пустой)
# age - целое число
# balance - целое число (не пустой)

cursor.execute('''
create table if not exists Users(
id INTEGER primary key,
username text not null,
email text not null,
age integer,
balance integer not null
)
''')

#Заполните её 10 записями:
for i in range(1,11):
    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",(f'User{i}', f'example{i}@gmail.com', f'{i*10}', '1000'))

#Обновите balance у каждой 2ой записи начиная с 1ой на 500:
cursor.execute('Update Users set balance = ? where (id % ? = 1)', (500,2))

#Удалите каждую 3ую запись в таблице начиная с 1ой:
cursor.execute('Delete  from Users where (id % ? = 1)', (3,))

# Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>'''
cursor.execute('Select username, email, age, balance from Users where age != ?',(60,))
users_not_60 = cursor.fetchall()
for user in users_not_60:
    print(f'Имя: <{user[0]}> | Почта: <{user[1]}> | Возраст: <{user[2]}> | Баланс: <{user[3]}>')
connection.commit()
connection.close()
