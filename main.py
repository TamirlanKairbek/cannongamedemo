from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty


class PongBall(Widget):
    velocity_x = NumericProperty(0)  # Горизонтальная скорость мяча
    velocity_y = NumericProperty(0)  # Вертикальная скорость мяча
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def __init__(self, **kwargs):
        super(PongBall, self).__init__(**kwargs)
        self.size_hint = (None, None)  # Отключаем автоматическое изменение размера
        self.size = (50, 50)  # Устанавливаем размер мяча (например, 50x50)

    def move(self, dt):  # Добавляем аргумент dt (время прошедшее с предыдущего обновления)
        self.pos = Vector(*self.velocity) + self.pos

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):  # Проверяем, касается ли касание мяча
            self.start_pos = touch.pos  # Устанавливаем начальную позицию натягивания мяча
            self.is_dragging = True  # Устанавливаем флаг, что мяч натягивается
            self.velocity = (0, 0)  # Обнуляем скорость мяча

    def on_touch_move(self, touch):
        if self.is_dragging:  # Если мяч натягивается
            self.end_pos = touch.pos  # Обновляем конечную позицию натягивания мяча

    def on_touch_up(self, touch):
        if self.is_dragging:  # Если мяч был натянут
            self.is_dragging = False  # Сбрасываем флаг натягивания мяча
            self.move_ball()  # Запускаем движение мяча

    def move_ball(self):
        direction = Vector(*self.end_pos) - Vector(*self.start_pos)  # Вычисляем направление движения
        self.velocity = direction * -0.05  # Задаем скорость мяча на основе направления натягивания

class PongApp(App):
    def build(self):
        ball = PongBall()
        ball.pos = (100, 100)  # Устанавливаем начальное положение мяча
        Clock.schedule_interval(ball.move, 1.0 / 60.0)  # Запускаем движение мяча
        return ball

if __name__ == '__main__':
    PongApp().run()