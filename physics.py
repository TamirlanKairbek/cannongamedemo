from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.graphics import Color, Ellipse
from kivy.vector import Vector
from pymunk import Space, Body, Circle, Segment


class CannonGame(Widget):
    ball_radius = NumericProperty(25)

    def __init__(self, **kwargs):
        super(CannonGame, self).__init__(**kwargs)
        self.space = Space()
        self.space.gravity = (0, -1000)  # установка гравитации
        self.ball_body = Body(1, 100, body_type=Body.DYNAMIC)
        self.ball_shape = Circle(self.ball_body, self.ball_radius)
        self.ball_shape.density = 1
        self.ball_shape.elasticity = 0.8
        self.ball_body.position = (self.width / 4, self.height / 2)
        self.space.add(self.ball_body, self.ball_shape)
        self.add_widget(self.ball_shape)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            impulse = Vector(touch.pos) - Vector(self.ball_body.position)
            impulse *= 0.05  # масштабируем вектор импульса
            self.ball_body.apply_impulse(impulse)
    
    def update(self, dt):
        self.space.step(dt)
        # Обновление позиции графического объекта шара
        self.ball_shape.pos = self.ball_body.position - Vector(self.ball_radius, self.ball_radius)


class CannonApp(App):
    def build(self):
        game = CannonGame()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    CannonApp().run()
