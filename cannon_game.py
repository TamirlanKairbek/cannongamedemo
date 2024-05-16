from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.vector import Vector
from physics import CannonPhysics  # Импорт класса с физикой


class CannonGame(Widget):
    ball_radius = NumericProperty(25)

    def __init__(self, **kwargs):
        super(CannonGame, self).__init__(**kwargs)
        self.physics = CannonPhysics()  # Создание экземпляра класса с физикой

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.physics.shoot_ball(touch.pos)  # Вызов метода класса с физикой для запуска шарика
    
    def update(self, dt):
        self.physics.update(dt)  # Обновление физики игры


class CannonApp(App):
    def build(self):
        game = CannonGame()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game
