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
import rt_with_exceptions as rt
import logging
import unittest

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                        encoding='UTF-8', format='%(asctime)s | %(levelno)s | %(levelname)s | %(message)s')

class RunnerTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        try:
            r1 = rt.Runner('Alex', speed=-5)
            for _ in range(5):
                r1.walk()
            self.assertEqual(r1.distance, 25)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner")


    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе заморожены")
    def test_run(self):
        try:
            r2 = rt.Runner(name=3654351)
            for _ in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner")


    @unittest.skipIf(is_frozen == False, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        r3 = rt.Runner(name='Emma')
        r4 = rt.Runner(name='Olivia')
        for _ in range(10):
            r3.walk()
            r4.run()
        self.assertNotEqual(r3.distance, r4.distance)
        logging.info("tournament")
