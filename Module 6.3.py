class Horse:
    def __init__(self, x_distance=0, y_distance, sound='Frrr'):
        self.x_distance = x_distance  # пройденный путь
        self.sound = sound # звук, который издаёт лошадь.
        super().__init__(y_distance, sound)
        super().fly()

    def run(self, dx):
        self.x_distance += dx



class Eagle:

    def __init__(self, y_distance = 0, sound = 'I train, eat, sleep, and repeat'):
        self.y_distance = y_distance  # высота полёта
        self.sound = sound  # звук, который издаёт орёл.

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self, x_distance, y_distance, sound):
        super().__init__(x_distance, y_distance, sound)
        super().fly()
        super().run()

    def move(self, dx, dy):
        self.run()
        self.fly()

    def get_pos(self):  # возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
        print(tuple(self.x_distance, self.y_distance))

    def voice(self):  # который печатает значение унаследованного атрибута sound.
        print(self.sound)

# h1 = Horse()
e1 = Eagle()
# p1 = Pegasus()

# print(p1.get_pos())
# p1.move(10, 15)
# print(p1.get_pos())
# p1.move(-5, 20)
# print(p1.get_pos())
#
# p1.voice()
print(Pegasus.mro())

print(e1.y_distance, e1.sound)
