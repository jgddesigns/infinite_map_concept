from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty
)



class Map(Widget):
    total_x = 0
    total_y = 0
    current_coords = [0, 0]
    bg = ObjectProperty(None)




    def move_map(self, pos): 
        try:          
                if pos[0] < 0:
                        self.total_x -= 1
                        self.set_map([self.total_x, self.total_y], True)
                        App.get_running_app().main.player.pos = [App.get_running_app().default_width - App.get_running_app().main.player.size[1], pos[1]]
                        return True

                if pos[0] + App.get_running_app().main.player.size[0] > App.get_running_app().default_width:
                        self.total_x += 1
                        self.set_map([self.total_x, self.total_y], True)
                        App.get_running_app().main.player.pos = [0, pos[1]]
                        return True

                if pos[1] < 0:
                        self.total_y -= 1
                        self.set_map([self.total_x, self.total_y], False)
                        App.get_running_app().main.player.pos = [pos[0], App.get_running_app().default_height - App.get_running_app().main.player.size[0]]
                        return True

                if pos[1] + App.get_running_app().main.player.size[1] > App.get_running_app().default_height:
                        self.total_y += 1
                        self.set_map([self.total_x, self.total_y], False)
                        App.get_running_app().main.player.pos = [pos[0], 0]
                        return True

                return False
        
        except Exception as e:
            print("\n\nError in 'Map' Class - 'move_map' Function", e)



    def set_map(self, coords, type):
        try:
                self.current_coords = coords
                if type:
                        App.get_running_app().main.key.traverse()
                else:
                        App.get_running_app().main.key.reverse()

                App.get_running_app().main.draw.draw_shapes()

        except Exception as e:
            print("\n\nError in 'Map' Class - 'set_map' Function", e)