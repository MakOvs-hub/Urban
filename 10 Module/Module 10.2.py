import time
from threading import Thread


class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name} на нас напали!!')
        enemy = 100
        count = 0
        while True:
            time.sleep(1)
            count += 1
            m = enemy - self.power
            if m >= 0:
                print(f"{self.name} сражается {count} дня(-ей), осталось {m} воинов.")
                yield enemy
            else:
                print(f"{self.name} одержал победу спустя {count} дня(-ей)!!")
                break


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
