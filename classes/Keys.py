from random import randint
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window



class Keys(Widget):
    map_keys = []
    base_keys = None
    key_size = 9
    current_x_key = 1
    current_y_key = 1
    min_key_value = 1
    max_key_value = 999




    def __init__(self, **kwargs):
        super().__init__(**kwargs)




    def set_key(self):
        try:
            keys = self.random_keys()
            self.map_keys = keys
        
            self.base_keys = keys

        except Exception as e:
            print("\n\nError in 'Calculations' Class - 'set_key' Function", e)


    def random_keys(self):
        try:
            keys = []
            while len(keys) < 9:
                keys.append(randint(self.min_key_value, self.max_key_value))
            return keys
        
        except Exception as e:
            print("\n\nError in 'Keys' Class - 'random_keys' Function", e) 


    def traverse(self):
        try:
            x = App.get_running_app().main.map.current_coords[0]
            y = App.get_running_app().main.map.current_coords[1]

            if x == 0 and y == 0:
                self.map_keys = self.base_keys
                return True
            
            if x == 0 and y > 0:
                x = int(str(self.base_keyss[0])[:1])
            
            if x == 0 and y < 0:
                x = int(str(self.base_keys[1])[:1])

            if x > 0 and y == 0:
                y = int(str(self.base_keys[2])[:1])

            if x < 0 and y == 0:
                y = int(str(self.base_keys[3])[:1])   

            if x + y == 0:
                x = abs(x)
                y = int(str(self.base_keys[4])[:1])    

            keys = []

            i = 0
            while len(keys) < self.key_size:
                num = self.base_keys[i] * (x + y) * x
                new_num = num
                while new_num > self.max_key_value:
                    new_num = new_num - self.max_key_value
                num = abs(new_num)
                keys.append(num)
                i += 1

            self.map_keys = keys    

        except Exception as e:
            print("\n\nError in 'Keys' Class - 'traverse' Function", e) 
    

    def reverse(self):
        try:
            x = App.get_running_app().main.map.current_coords[0]
            y = App.get_running_app().main.map.current_coords[1]

            if x == 0 and y == 0:
                self.map_keys = self.base_keys
                return True
            
            if x == 0 and y > 0:
                x = int(str(self.base_keys[0])[:1])
            
            if x == 0 and y < 0:
                x = int(str(self.base_keys[1])[:1])

            if x > 0 and y == 0:
                y = int(str(self.base_keys[2])[:1])

            if x < 0 and y == 0:
                y = int(str(self.base_keys[3])[:1])   

            if x + y == 0:
                x = abs(x)
                y = int(str(self.base_keys[4])[:1])     
            
            keys = []

            i = 0
            while len(keys) < self.key_size:
                num = abs(self.base_keys[i] * (x + y) * y)
                new_num = num
                while new_num > self.max_key_value:
                    new_num = new_num - self.max_key_value
                num = abs(new_num)
                keys.append(num)
                i += 1

            self.map_keys = keys

        except Exception as e:
            print("\n\nError in 'Keys' Class - 'reverse' Function", e) 