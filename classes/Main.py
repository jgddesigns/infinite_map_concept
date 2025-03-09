from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty
)

from classes.Keys import Keys
from classes.Draw import Draw
from classes.Player import Player
from classes.Map import Map


class Main(Widget):
    key = None
    draw = None
    player = None
    map = None
    classes = None
    app = None

    player = ObjectProperty(None)




    def __init__(self, **kwargs):
        try:
            super().__init__(**kwargs)
            self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
            self._keyboard.bind(on_key_down=self._on_keyboard_down)        

            self.app = App.get_running_app()

            self.key = Keys()
            self.draw = Draw()
            self.player = Player()
            self.map = Map()

            self.add_widget(self.key)
            self.add_widget(self.draw)
            self.add_widget(self.player)
            self.add_widget(self.map)

        except Exception as e:
            print("\n\nError in 'Main' Class - '__init__' Function", e) 


    def start(self):
        try:
            self.key.set_key()
            self.draw.draw_shapes()
            self.player.pos[0] = 375
            self.player.pos[1] = 335

        except Exception as e:
            print("\n\nError in 'Main' Class - 'start' Function", e) 


    def _keyboard_closed(self):
        try:
            self._keyboard.unbind(on_key_down=self._on_keyboard_down)
            self._keyboard = None

        except Exception as e:
            print("\n\nError in 'Main' Class - '_keyboard_closed' Function", e) 


    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        try:
            prev_x = self.player.pos[0]
            prev_y = self.player.pos[1]

            if keycode[1] == 'right':
                self.player.pos[0] += 25

            if keycode[1] == 'left':
                self.player.pos[0] -= 25

            if keycode[1] == 'up':
                self.player.pos[1] += 25

            if keycode[1] == 'down':
                self.player.pos[1] -= 25

            self.player_move(self.player.pos[0], self.player.pos[1], prev_x, prev_y)

        except Exception as e:
            print("\n\nError in 'Main' Class - '_keyboard_down' Function", e) 


    def player_move(self, x, y, prev_x, prev_y):
        try:
            if x + self.player.size[0] > self.width:
                self.map.move_map([x, y])

            if x < 0:
                self.map.move_map([x, y])

            if y + self.player.size[1] > self.height:
                self.map.move_map([x, y])

            if y < 0:
                self.map.move_map([x, y])

        except Exception as e:
            print("\n\nError in 'Main' Class - 'player_move' Function", e) 