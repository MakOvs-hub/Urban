"""
Реализуем принцип работы ресторана, представив поваров как классы и настроив взаимодействие между ними.
"""

import random
import time
from threading import Thread
import queue

class Bulki(Thread):
    def __init__(self, queue):
        self.queue = queue #принимает объект очереди
        super().__init__()

    def run(self): # реализуем метод run, чтобы метод start отработал
        while True: # бесконечно делает булки
            time.sleep(random.randint(1,10)) #имитация работы повара
            if random.random() > 0.9: # возвращает случайное число от 0 до 1 float
                # и если данное число будет больше 0.9, т.е. с вероятностью 10% выдаст необходимую строчку кода
                self.queue.put("Подгорелая булка")
            else:
                self.queue.put("Поджаренная булка")


class Kotletka(Thread):
    def __init__(self, queue, count):
        self.queue = queue #принимает объект очереди
        self. count = count#будем контролировать количество сделанных бургеров
        super().__init__()

    def run(self):
        while self.count:#в данном случае производится подсчет
            print(self.queue.qsize())  # печатает нам размер нашей очереди на каждом шаге
            bulka = self.queue.get(timeout=20)#может принимать аргументом timeout максимально ограничивает
            # время ожидания объекта в очереди, иначе выбросит ошибку пустой очереди empty
            if bulka == 'Поджаренная булка':
                time.sleep(random.randint(1,10))
                self.count -= 1
            print(f"Булок к приготовлению осталось: {self.count}")

queue = queue.Queue(maxsize=50)#может принимать аргументом maxsize максимально ограничивающий параметр очереди

t1 = Bulki(queue)
t2 = Kotletka(queue, 20)#передаем в котлету count, как необходимое к производству количество бургеров

t1.start()
t2.start()

t1.join()
t2.join()