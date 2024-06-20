'''
Домашнее задание по уроку "Перегрузка операторов"

Создайте новый проект в PyCharm
Запустите созданный проект
Ваша задача:
Создайте новый класс Building
Создайте инициализатор для класса Building, который будет задавать целочисленный атрибут этажности self.numberOfFloors
и строковый атрибут self.buildingType
Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
Полученный код напишите в ответ к домашнему заданию
'''

class Building:
    def __init__(self, numberOfFloors: int, buildingType: str):
        self. numberOfFloors = numberOfFloors
        self. buildingType = buildingType

    def __eq__(self, other):
        return self.buildingType == other.buildingType or self.numberOfFloors == other.numberOfFloors
# меняем or на and и получаем строгое соответствие обоих параметров

H1 = Building( 5, "Хрущевка")
H2 = Building( 22, "Высотка")
H3 = Building(9, "Хрущевка")

print(H1 == H2)
print(H2 == H3)
print(H1 == H3)





