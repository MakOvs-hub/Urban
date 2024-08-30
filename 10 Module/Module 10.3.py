import random
import threading
import time

lock = threading.Lock()


class Bank(threading.Thread):
    def __init__(self):
        super().__init__()
        self.balance = 0

    def deposit(self):
        for i in range(100):
            x = random.randint(50, 500)
            if self.balance >= 500 and lock.locked():
                lock.release()
                self.balance += x
                print(f'Пополнение: {x}. Баланс: {self.balance}.')
                time.sleep(0.0001)
            else:
                self.balance += x
                print(f'Пополнение: {x}. Баланс: {self.balance}.')
                time.sleep(0.0001)

    def take(self):
        for i in range(100):
            y = random.randint(50, 500)
            print(f"Запрос на {y}.")
            if y <= self.balance:
                self.balance -= y
                print(f'Снятие: {y}. Баланс: {self.balance}.')
            else:
                print(f'Запрос отклонён, недостаточно средств.')
                lock.acquire()
                time.sleep(0.0001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
