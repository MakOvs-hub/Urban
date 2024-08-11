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
    for i in range(len(text)):
        m = text[i]
        yield m
    if len(m) < len(text):
        for j in range(len(text) - 1):
            m = text[j]
            b = text[j+1]
            if m != b:
                yield m+b
    if len(m+b) < len(text):
        for k in range(len(text)-2):
            m = text[k]
            b = text[k + 1]
            f = text[k + 2]
            if f not in (m+b):
                yield m+b+f

a = all_variants("abc")
for i in a:
    print(i)