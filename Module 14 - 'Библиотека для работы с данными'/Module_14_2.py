import sqlite3

# Для решения необходимо дополнить существующий код из Module_14_1
# Удалите из базы данных not_telegram.db запись с id = 6.
connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('DELETE FROM Users WHERE (id = ?)', (6,))

# Подсчитать общее количество записей.
cursor.execute('SELECT COUNT(*) FROM Users')
res_count = cursor.fetchone()[0]
print(res_count)

# Посчитать сумму всех балансов.
cursor.execute('SELECT SUM(balance) FROM Users')
res_sum = cursor.fetchone()[0]
print(res_sum)

# Вывести в консоль средний баланс всех пользователей.
cursor.execute('SELECT AVG(balance) FROM Users')
res_avg = cursor.fetchone()[0]
print(res_avg)

connection.commit()
connection.close()
