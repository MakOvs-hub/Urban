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
        sleep(randint(3,10))
        Table.guest = None


class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables



    def guest_arrival(self, *guests):
        for table in list(tables):
            for j in guests:
                if table.guest != None:
                    print(f' {j.name} в очереди')
                    queue.Queue.put(j) # не кладет в очередь
                    # th = threading.Thread(target=Guest.run, args=(*guests,))
                    # th.start()
                    # th.join()
                else:
                    table.guest = j.name
                    print(f' {j.name} сел(-а) за стол номер {table.number}')
                    #нужен ли лок потоков


    def discuss_guests(self):
        if not queue.empty() or thread.is_alive():
            print(f'{Guest.name} покушал(-а) и ушёл(ушла).\n Стол номер {Table()} свободен.')
            table.guest = None
            queue.put(Table())
        elif not queue.empty() or table.guest == None:
            queue.get(Table())
            print(f'{Guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {Table()}')
            th = threading.Thread(target=Guest.run, args=(tables,))
            th.start()
            th.join()  # нужен ли лок потоков

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
# cafe.discuss_guests()
