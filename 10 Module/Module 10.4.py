import threading
import queue
from time import sleep
from random import randint


class Table:
    def __init__(self, number):
        self.number = number #номер стола
        self.guest = None #гость, который сидит за этим столом

class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print('Please wait.')
        sleep(randint(3,10))
        print('Your turn.')

class Cafe(queue):
    def __init__(self):
        super().__init__()
        self.queue = queue


    def guest_arrival(self, guests):
        if queue.empty():
            print(f' {self.guests} в очереди')
        elif queue.get(Table()):
            print(f' {self.guests} сел(-а) за стол номер {Table()}')
    def discuss_guests(self):
        if not queue.empty() or thread.is_alive():
            print(f'{Guest.name} покушал(-а) и ушёл(ушла).\n Стол номер {Table()} свободен.')
            table.guest = None
            queue.put(Table())
        elif not queue.empty() or table.guest == None:
            queue.get(Table())
            print(f'{Guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {Table()}')
            tr = threading.Thread(target=Guest.run(), args = (Guest.name,))
            tr.start()
            tr.join()

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()