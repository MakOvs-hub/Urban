'''Домашнее задание по уроку "Различие атрибутов класса и экземпляра"

Создайте новый проект в PyCharm
Запустите созданный проект
Ваша задача:
Создайте новый класс Buiding с атрибутом total
Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных объектов класса Building total
В цикле создайте 40 объектов класса Building и выведите их на экран командой print
Полученный код напишите в ответ к домашнему заданию'''



class Buiding:
    total = 0

    def __init__(self, name):
        self.name = name

while Buiding.total < 40:
     house = Buiding(f'Строение {Buiding.total}')
     Buiding.total += 1


print(house)
print(Buiding.total)
