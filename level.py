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
            self.rect = Rectangle(size=(20, 20), pos=self.pos)  # Уменьшаем размер целей до 20x20
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
            target = Target(pos=pos, size=(20, 20))  # Располагаем мишени в фиксированных местах на уровне
            self.add_widget(target)  # Добавляем мишени в уровень
            self.add_targets_around(pos)  # Добавляем цели вокруг текущей цели

    def add_targets_around(self, pos):
        offsets = [(-30, 0), (30, 0), (0, -30), (0, 30), (-30, -30), (30, -30), (-30, 30), (30, 30)]
        for offset in offsets:
            new_pos = (pos[0] + offset[0], pos[1] + offset[1])
            target = Target(pos=new_pos, size=(20, 20))  # Создаем новую цель
            self.add_widget(target)  # Добавляем новую цель в уровень

    def check_collision(self, ball):
        for target in self.children[:]:
            if ball.collide_widget(target):
                self.remove_widget(target)
                ball.reset_ball()
                break
            
class Cannon(Widget):
    pass
