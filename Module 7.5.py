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


