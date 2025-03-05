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

    player = ObjectProperty(None)
    classes = None
    app = None




    def __init__(self, **kwargs):
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




    def start(self):
        self.key.set_key()
        self.draw.draw_shapes()
        self.player.pos[0] = 375
        self.player.pos[1] = 335


    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None


    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
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


    def player_move(self, x, y, prev_x, prev_y):
        if x + self.player.size[0] > self.width:
            print('right')
            self.map.move_map([x, y])

        if x < 0:
            print('left')
            self.map.move_map([x, y])

        if y + self.player.size[1] > self.height:
            print('up')
            self.map.move_map([x, y])

        if y < 0:
            print('down')
            self.map.move_map([x, y])