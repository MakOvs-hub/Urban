'''
Цель задания:

Освоить работу с файловой системой в Python, используя модуль os.
Научиться применять методы os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize и использование модуля time для корректного отображения времени.

Задание:

Создайте новый проект или продолжите работу в текущем проекте.
Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
Примените os.path.join для формирования полного пути к файлам.
Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
Используйте os.path.getsize для получения размера файла.
Используйте os.path.dirname для получения родительской директории файла.
'''
import os
import time

for root, dirs, files in os.walk('.'):
    for i in files:
        filepath = os.getcwd()
        filetime = os.path.getmtime()
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize()
        parent_dir = os.path.dirname()
        print(f'Обнаружен файл: {i}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')


