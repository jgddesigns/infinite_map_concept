from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty
)

class Player(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)




    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rgba = (1, 1, 1, 1)


        

    def move(self):
        try:
            self.pos = Vector(*self.velocity) + self.pos

        except Exception as e:
            print("\n\nError in 'Player' Class - 'move' Function", e)