from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.config import Config

Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '700')


class PongBall(Widget):
    velocity_x = NumericProperty(0)  # Горизонтальная скорость мяча
    velocity_y = NumericProperty(0)  # Вертикальная скорость мяча
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    start_pos = ()  # Начальная позиция натягивания мяча
    end_pos = ()  # Конечная позиция натягивания мяча
    is_dragging = False  # Флаг для отслеживания натягивания мяча
    is_launched = False  # Флаг для отслеживания запуска мяча
    acceleration = 0

    def __init__(self, **kwargs):
        super(PongBall, self).__init__(**kwargs)
        self.size_hint = (None, None)  # Отключаем автоматическое изменение размера
        self.size = (20, 20)  # Устанавливаем размер мяча (например, 50x50)

    def move(self, dt):
        self.velocity_y -= self.acceleration  # Добавляем гравитацию
        self.pos = Vector(*self.velocity) + self.pos  # Двигаем мяч

        if self.y > 700 or self.y < 0 or self.x > 1000 or self.x < 0:
            self.pos = (100, 100)
            self.velocity = Vector(0, 0)
            self.acceleration = 0   
            self.is_launched = False   

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and not self.is_launched:  # Проверяем, касается ли касание мяча и мяч не был запущен
            self.start_pos = touch.pos  # Устанавливаем начальную позицию натягивания мяча
            self.is_dragging = True  # Устанавливаем флаг, что мяч натягивается

    def on_touch_move(self, touch):
        if self.is_dragging:  # Если мяч натягивается
            self.end_pos = touch.pos  # Обновляем конечную позицию натягивания мяча

    def on_touch_up(self, touch):
        if self.is_dragging:  # Если мяч был натянут
            self.is_dragging = False  # Сбрасываем флаг натягивания мяча
            self.move_ball()  # Запускаем движение мяча

    def move_ball(self):
        direction = Vector(*self.end_pos) - Vector(*self.start_pos)  # Вычисляем направление движения
        self.velocity = direction * -0.1  # Задаем скорость мяча на основе направления натягивания
        self.is_launched = True  # Устанавливаем флаг, что мяч был запущен
        self.acceleration = 0.2


class PongApp(App):
    def build(self):
        ball = PongBall()
        ball.pos = (100, 100)  # Устанавливаем начальное положение мяча
        Clock.schedule_interval(ball.move, 1.0 / 60.0)  # Запускаем движение мяча
        return ball


if __name__ == '__main__':
    PongApp().run()