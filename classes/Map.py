from kivy.app import App
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, ListProperty
)



class Map(Widget):
    bg = ObjectProperty(None)
    total_x = 0
    total_y = 0
    current_coords = [0, 0]


    def change_map(self, pos):
        pass


    def move_map(self, pos): 
        print("x - " + str(pos[0]))
        print("y - " + str(pos[1]))
        print("total x - " + str(self.total_x))
        print("total y - " + str(self.total_y))
                         
        if pos[0] < 0:
                self.total_x -= 1
                self.set_map([self.total_x, self.total_y], True)
                print("after x - " + str(self.total_x))
                print("after y - " + str(self.total_y))
                App.get_running_app().main.player.pos = [App.get_running_app().default_width - App.get_running_app().main.player.size[1], pos[1]]
                return True

        if pos[0] + App.get_running_app().main.player.size[0] > App.get_running_app().default_width:
                self.total_x += 1
                self.set_map([self.total_x, self.total_y], True)
                print("after x - " + str(self.total_x))
                print("after y - " + str(self.total_y))
                App.get_running_app().main.player.pos = [0, pos[1]]
                return True

        if pos[1] < 0:
                self.total_y -= 1
                self.set_map([self.total_x, self.total_y], False)
                print("after x - " + str(self.total_x))
                print("after y - " + str(self.total_y))
                App.get_running_app().main.player.pos = [pos[0], App.get_running_app().default_height - App.get_running_app().main.player.size[0]]
                return True

        if pos[1] + App.get_running_app().main.player.size[1] > App.get_running_app().default_height:
                self.total_y += 1
                self.set_map([self.total_x, self.total_y], False)
                print("after x - " + str(self.total_x))
                print("after y - " + str(self.total_y))
                App.get_running_app().main.player.pos = [pos[0], 0]
                return True

        print("after x - " + str(self.total_x))
        print("after y - " + str(self.total_y))
        return False



    def set_map(self, coords, type):
        self.current_coords = coords
        if type:
                App.get_running_app().main.key.test_traverse()
        else:
                App.get_running_app().main.key.test_reverse()

        App.get_running_app().main.draw.draw_shapes()
          
          

                   

      


        
        


