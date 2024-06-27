"""На основе произвольного числа подобрать пароль из всех возможных кратных комбинаций сумм переменных
в пределах диапазона."""

def generate_password(n):
    password = ''
 # создаем матрицу на основе случайного значения, где n - количество шагов, i - начальная переменная, j- переменная номинального шага
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                password += str(i) + str(j) + " "
    return password

for n in range(3, 21): # условие задания произвольного числа от 3 до 20.
        password = generate_password(n)
        print(f"{n} - {password}")
