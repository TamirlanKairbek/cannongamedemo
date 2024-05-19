from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.graphics import Rectangle, Color, Line

class Laser(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    start_pos = ()
    end_pos = ()
    is_dragging = False
    is_launched = False
    initial_pos = (200, 200)  

    def __init__(self, **kwargs):
        super(Laser, self).__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (20, 20)  
        self.pos = self.initial_pos
        self.path_points = []  

        with self.canvas:
            Color(1, 0, 0)
            self.rectangle = Rectangle(pos=self.pos, size=self.size)
            Color(1, 0, 0)
            self.line = Line(points=[], width=6)  # Уменьшаем толщину следа от лазера
        self.bind(pos=self.update_graphics_pos, size=self.update_graphics_pos)
        Clock.schedule_interval(self.move, 1.0 / 60.0)

    def update_graphics_pos(self, *args):
        self.rectangle.pos = self.pos
        self.rectangle.size = self.size

    def move(self, dt):
        self.pos = Vector(*self.velocity) + self.pos

        if self.is_launched:
            self.path_points.extend([self.center_x, self.center_y])
            self.line.points = self.path_points  

        if self.y > 700 or self.y < 0 or self.x > 1000 or self.x < 0:
            self.reset_laser()

        if self.parent:
            self.parent.on_collision()

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
            self.launch()

    def launch(self):
        direction = Vector(*self.end_pos) - Vector(*self.start_pos)
        self.velocity = direction * -0.05  
        self.is_launched = True
        self.path_points = [self.center_x, self.center_y]  

    def reset_laser(self):
        self.pos = self.initial_pos
        self.velocity = Vector(0, 0)
        self.is_launched = False
        self.path_points = []
        self.line.points = self.path_points  

class Game(Widget):
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self.laser = Laser()
        self.add_widget(self.laser)

    def check_collision(self, widget):
        pass  

class LaserApp(App):
    def build(self):
        return Game()

if __name__ == '__main__':
    LaserApp().run()
