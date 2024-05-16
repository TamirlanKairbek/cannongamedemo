from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.config import Config

Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '700')


class PongBall(Widget):
    velocity_x = NumericProperty(0)  
    velocity_y = NumericProperty(0)  
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    start_pos = ()  
    end_pos = ()  
    is_dragging = False  
    is_launched = False  
    acceleration = 0

    def __init__(self, **kwargs):
        super(PongBall, self).__init__(**kwargs)
        self.size_hint = (None, None)  
        self.size = (20, 20)

    def move(self, dt):
        self.velocity_y -= self.acceleration  
        self.pos = Vector(*self.velocity) + self.pos  

        if self.y > 700 or self.y < 0 or self.x > 1000 or self.x < 0:
            self.pos = (100, 100)
            self.velocity = Vector(0, 0)
            self.acceleration = 0   
            self.is_launched = False   

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and not self.is_launched:
            self.start_pos = touch.pos  
            self.is_dragging = True  

    def on_touch_move(self, touch):
        if self.is_dragging:  
            self.end_pos = touch.pos  

    def on_touch_up(self, touch):
        if self.is_dragging:  
            self.is_dragging = False  
            self.move_ball()

    def move_ball(self):
        direction = Vector(*self.end_pos) - Vector(*self.start_pos)  
        self.velocity = direction * -0.1 
        self.is_launched = True 
        self.acceleration = 0.2


class PongApp(App):
    def build(self):
        ball = PongBall()
        ball.pos = (100, 100)  
        Clock.schedule_interval(ball.move, 1.0 / 60.0)  
        return ball


if __name__ == '__main__':
    PongApp().run()