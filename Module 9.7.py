'''
Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое",
если результат 1ой функции будет простым числом и "Составное" в противном случае.
Пример:
result = sum_three(2, 3, 6)
print(result)

Результат консоли:
Простое
11
'''


def is_prime(func):
    def simple(*args):
        list1 = []
        result2 = func(*args)
        for i in range(1, result2):
            if result2 % i == 0:
                list1.append(i)
        if len(list1) == 1:
            print('Простое')
        else:
            print('Составное')
        return result2
    return simple

@is_prime
def sum_three(*arqs):
    sum_ = 0
    for i in arqs:
        sum_ += i
    return sum_

result = sum_three(2, 3, 6)
print(result)
