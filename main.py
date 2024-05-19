from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock
from kivy.config import Config
from kivy.lang import Builder
from kivy.vector import Vector

from cannon import PongBall
from level import Level
from laser import Laser
from bombshell import Bombshell  # Импортируем Bombshell

Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '700')
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'minimum_width', '1000')
Config.set('graphics', 'minimum_height', '700')

Builder.load_file('pong.kv')

class Game(RelativeLayout):
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        
        self.level = Level()  # Создаем экземпляр уровня
        self.ball = PongBall()  # Создаем экземпляр пушки
        self.ball.pos = (100, 100)  # Устанавливаем начальное положение мяча
        self.laser = Laser()  # Создаем экземпляр лазера
        self.laser.pos = (200, 200)  # Устанавливаем начальное положение лазера
        self.bombshell = Bombshell()
        self.bombshell.pos = (500, 300)  # Изменяем начальную позицию бомбы

        # Добавляем уровень, пушку, лазер и бомбу на главный виджет
        self.add_widget(self.level)
        self.add_widget(self.ball)
        self.add_widget(self.laser)
        self.add_widget(self.bombshell)

        # Запускаем движение мяча, лазера и бомбы
        Clock.schedule_interval(self.ball.move, 1.0 / 60.0)
        Clock.schedule_interval(self.laser.move, 1.0 / 60.0)
        Clock.schedule_interval(self.bombshell.move, 1.0 / 60.0)

    def on_collision(self):
        self.bombshell.explode()  # Передача аргумента dt
        for target in self.level.children:
            if self.ball.collide_widget(target):
                self.level.remove_widget(target)
                self.ball.reset_ball()
            if self.laser.collide_widget(target):
                self.level.remove_widget(target)
                self.laser.reset_laser()
            if self.bombshell.collide_widget(target):
                self.level.remove_widget(target)
                self.bombshell.explode()

class MyApp(App):
    def build(self):
        return Game()

if __name__ == '__main__':
    MyApp().run()
