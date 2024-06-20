'''Создайте новый класс House
Создайте инициализатор для класса House, который будет задавать атрибут этажности self.numberOfFloors = 0
Создайте метод setNewNumberOfFloors(floors), который будет изменять атрибут numberOfFloors на параметр floors и выводить в консоль numberOfFloors
Полученный код напишите в ответ к домашнему заданию'''


class House:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = 0
        self.setNewNumberOfFloors(numberOfFloors)

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(f"В доме {self.numberOfFloors} этажей")


H1 = House(7)