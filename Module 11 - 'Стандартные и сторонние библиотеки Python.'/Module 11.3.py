'''
Цель задания:

Закрепить знания об интроспекции в Python.
Создать персональную функции для подробной интроспекции объекта.

Задание:
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента и проводит интроспекцию этого объекта,
чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
  - Другие интересные свойства объекта, учитывая его тип (по желанию).


Пример работы:
number_info = introspection_info(42)
print(number_info)

Вывод на консоль:
{'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}
'''
import sys
import inspect
import pprint


class ObjIter:

    def __init__(self):
        self.attrib = 1

    def introspection_info(self, obj):
        self.attrib = obj
        print(type(ex.attrib))
        print(hasattr(ex, 'attrib'))
        print(getattr(ex, 'attrib_2', "Oooops. Attrib_2 not exist."))
        print(inspect.ismethoddescriptor(ex))


ex = ObjIter()


ex.introspection_info(42)
ex.introspection_info('String')
ex.introspection_info(list())
pprint.pprint(dir(ex))
pprint.pprint(sys.version_info)

