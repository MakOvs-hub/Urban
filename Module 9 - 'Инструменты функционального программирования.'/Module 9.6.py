"""
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
 при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации.
Пример результата выполнения программы:
Пример работы функции:
a = all_variants("abc")
for i in a:
print(i)
Вывод на консоль:
a
b
c
ab
bc
abc
"""


def all_variants(text):
    x = len(text) + 1
    for i in range(1, x):
        for j in range(x - i):
            yield text[j: j+i]

a = all_variants("abc")
for i in a:
    print(i)
