'''
Задача "Логирование бегунов":
Основное обновление - выбрасывание исключений, если передан неверный тип в name и если передано отрицательное значение в speed.

Для решения этой задачи вам понадобиться класс RunnerTest из предыдущей задачи.
В модуле tests_12_4.py импортируйте пакет logging и настройте basicConfig на следующие параметры:
Уровень - INFO
Режим - запись с заменой('w')
Название файла - runner_tests.log
Кодировка - UTF-8
Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.

Дополните методы тестирования в классе RunnerTest следующим образом:
test_walk:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте отрицательное значение в speed.
В блок try добавьте логирование INFO с сообщением '"test_walk" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверная скорость для Runner".
test_run:
Оберните основной код конструкцией try-except.
При создании объекта Runner передавайте что-то кроме строки в name.
В блок try добавьте логирование INFO с сообщением '"test_run" выполнен успешно'
В блоке except обработайте исключение соответствующего типа и логируйте его на уровне WARNING с сообщением "Неверный тип данных для объекта Runner".

'''

import logging
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8', format='%(asctime)s | %(levelno)s | %(levelname)s | %(message)s')
logging.critical('5')

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers



class RunnerTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        r1 = Runner(name='Alex')
        for _ in range(5):
            r1.walk()
        self.assertEqual(r1.distance, 25)
        print('logging.info("walk")')

    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе заморожены")
    def test_run(self):
        r2 = Runner(name='John')
        for _ in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)
        print('logging.info("run")')


    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        r3 = Runner(name='Emma')
        r4 = Runner(name='Olivia')
        for _ in range(10):
            r3.walk()
            r4.run()
        self.assertNotEqual(r3.distance, r4.distance)
        print('logging.info("tournament")')


if __name__ == '__main__':
    print('Абра-Кадабра')
    unittest.main()
    # logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
    #                     encoding='UTF-8', format='%(asctime)s | %(levelno)s | %(levelname)s | %(message)s')
    # logging.critical('5')

first = Runner('Вося', 10)
second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
t = Tournament(101, first, second)
print(t.start())




#Вариант с импортом файла.



import rt_with_exceptions as rt
import logging
import unittest

# logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8', format='%(asctime)s | %(levelno)s | %(levelname)s | %(message)s')
# logging.critical('5')

class RunnerTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        r1 = rt.Runner(name='Alex')
        for _ in range(5):
            r1.walk()
        self.assertEqual(r1.distance, 25)
        print('logging.info("walk")')

    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе заморожены")
    def test_run(self):
        r2 = rt.Runner(name='John')
        for _ in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)
        print('logging.info("run")')


    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        r3 = rt.Runner(name='Emma')
        r4 = rt.Runner(name='Olivia')
        for _ in range(10):
            r3.walk()
            r4.run()
        self.assertNotEqual(r3.distance, r4.distance)
        print('logging.info("tournament")')


if __name__ == '__main__':
    print('Абра-Кадабра')
    unittest.main()
    logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding='UTF-8', format='%(asctime)s | %(levelno)s | %(levelname)s | %(message)s')
    logging.critical('5')
