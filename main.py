from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.clock import Clock
from kivy.config import Config
from kivy.lang import Builder

from cannon import PongBall  # Импортируем класс PongBall из файла cannon.py
from level import Level  # Импортируем класс Level из файла level.py

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
        
        # Добавляем уровень и пушку на главный виджет
        self.add_widget(self.level)
        self.add_widget(self.ball)
        
        # Запускаем движение мяча
        Clock.schedule_interval(self.ball.move, 1.0 / 60.0)

class MyApp(App):
    def build(self):
        return Game()

if __name__ == '__main__':
    MyApp().run()
