import arcade

SCREEN_WIDTH = 800 # задаем размеры она и название
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Pong game'

class Bar(arcade.Sprite): # класс будет представлять ракетку и логику перемещений
    def __init__(self):
        super().__init__('bar.png', 0.15) # название файла, которое будет отвечать за наш спрайт, а scale — это будет масштаб

    def update(self):  # делаем мячик подвижным, добавляем изменение координат со временем
        self.center_x += self.change_x
        if self.right >= SCREEN_WIDTH: # устанавливаем ограничения спрайта по размеру экрана
            self.right = SCREEN_WIDTH
        if self.left <= 0:
            self.left = 0

class Ball(arcade.Sprite): # класс будет представлять мяч и логику перемещений
    def __init__(self):
        super().__init__('ball.png', 0.05)
        self.change_x = 5
        self.change_y = 5

    def update(self): # делаем мячик подвижным, добавляем изменение координат со временем
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.right >= SCREEN_WIDTH: # right - значение грани спрайта, соответсвенно справа и когда значение совпадает с экраном
            self.change_x = -self.change_x # спрайт меняет вектор движения
        if self.left <= 0: # левое значение грани спрайта
            self.change_x = -self.change_x
        if self.top >= SCREEN_HEIGHT: # top - значение грани спрайта, соответсвенно сверху фигуры и когда значение совпадает с экраном
            self.change_y = -self.change_y # спрайт меняет вектор движения
        if self.bottom <= 0: # нижнее значение
            self.change_y = -self.change_y # Мяч отскакивает от каждой стороны.


class Game(arcade.Window): # класс будет представлять наше главное окно
    def __init__(self, width, height, title):
        super().__init__(width, height, title) # ракетка появилась в нашей игре, значит, её нужно создать внутри нашего класса Game
        self.bar = Bar() # создадим нашу ракетку
        self.ball = Ball()  # создадим мяч
        self.setup()

    def setup(self): # определяет центр sprite - bar
        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = SCREEN_HEIGHT / 5
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2

    def on_draw(self): # отрисовка элементов на нашем окне
        self.clear((255,255,255)) # переопределим его и в этом методе вызовем метод clear(),
                                    # который отвечает за очистку нашего экрана и закрасит его белым, т.к. RGB == 255,255,255
        self.bar.draw() # отрисовка ракетки
        self.ball.draw() # отрисовка мяча

    def update(self, delta):
        if arcade.check_for_collision(self.bar, self.ball):
            self.ball.change_y = - self.ball.change_y # при столкновении (collision) двух спрайтов изменится вектор мяча
        self.ball.update()
        self.bar.update()

    def on_key_press(self, key: int, modifiers: int): # реализация управления с клавиатуры при нажатии
        if key == arcade.key.RIGHT:
            self.bar.change_x = 5
        if key == arcade.key.LEFT:
            self.bar.change_x = -5

    def on_key_release(self, key: int, modifiers: int): # реализация управления с клавиатуры при отпускании
        if key == arcade.key.RIGHT or key == arcade.key.LEFT:
            self.bar.change_x = 0

if __name__ == '__main__':
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()