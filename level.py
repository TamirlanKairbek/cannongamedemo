from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from random import randint
from kivy.config import Config

Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '700')
Config.set('graphics', 'resizable', '0')  # Запрещаем изменение размера окна
Config.set('graphics', 'minimum_width', '1000')  # Устанавливаем минимальную ширину окна
Config.set('graphics', 'minimum_height', '700')  # Устанавливаем минимальную высоту окна

class Target(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 1, 1)  # Белый цвет
            self.rect = Rectangle(size=(30, 30), pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class Level(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Определяем фиксированные позиции для трех мишеней
        positions = [(500, 300), (400, 600), (600, 200)]
        for pos in positions:
            target = Target(pos=pos, size=(30, 30))  # Располагаем мишени в фиксированных местах на уровне
            self.add_widget(target)  # Добавляем мишени в уровень

    def check_collision(self, ball):
        for target in self.children[:]:
            print(target)
            if ball.collide_widget(target):
                self.remove_widget(target)
                ball.reset_ball()
                break

class Cannon(Widget):
    pass
