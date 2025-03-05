from random import randint
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window



class Keys(Widget):
    map_keys = []
    base_key = None
    key_size = 9
    current_x_key = 1
    current_y_key = 1
    min_key_value = 1
    max_key_value = 999




    def __init__(self, **kwargs):
        super().__init__(**kwargs)




    def set_key(self):
        try:
            print("\n\n\n\n'Calculations' Class - 'set_key' Function")

            x_key = self.random_keys()
            self.map_keys = x_key
        
            self.base_key = self.map_keys

            print("\n\nadded base keys to main key")
            print(self.map_keys)

        except Exception as e:
            print("\n\nError in 'Calculations' Class - 'set_key' Function", e)


    def random_keys(self):
        keys = []
        while len(keys) < 9:
            keys.append(randint(self.min_key_value, self.max_key_value))
        return keys


    def test_traverse(self):
        x = App.get_running_app().main.map.current_coords[0]
        y = App.get_running_app().main.map.current_coords[1]

        if x == 0 and y == 0:
            print("\n\nnew key")
            print(self.base_key)
            self.map_keys = self.base_key
            return True
        
        if x == 0 and y > 0:
            x = int(str(self.base_key[0])[:1])
        
        if x == 0 and y < 0:
            x = int(str(self.base_key[1])[:1])

        if x > 0 and y == 0:
            y = int(str(self.base_key[2])[:1])

        if x < 0 and y == 0:
            y = int(str(self.base_key[3])[:1])   

        if x + y == 0:
            x = abs(x)
            y = int(str(self.base_key[4])[:1])    

        key = []

        i = 0
        while len(key) < self.key_size:
            num = self.base_key[i] * (x + y) * x
            new_num = num
            while new_num > self.max_key_value:
                new_num = new_num - self.max_key_value
            num = abs(new_num)
            key.append(num)
            i += 1

        print("\n\nnew key")
        print(key)
        self.map_keys = key    


    def test_reverse(self):
        x = App.get_running_app().main.map.current_coords[0]
        y = App.get_running_app().main.map.current_coords[1]

        if x == 0 and y == 0:
            print("\n\nnew key")
            print(self.base_key[0])
            self.map_keys = self.base_key[0]
            return True
        
        if x == 0 and y > 0:
            x = int(str(self.base_key[0])[:1])
        
        if x == 0 and y < 0:
            x = int(str(self.base_key[1])[:1])

        if x > 0 and y == 0:
            y = int(str(self.base_key[2])[:1])

        if x < 0 and y == 0:
            y = int(str(self.base_key[3])[:1])   

        if x + y == 0:
            x = abs(x)
            y = int(str(self.base_key[4])[:1])     
        
        key = []

        i = 0
        while len(key) < self.key_size:
            num = abs(self.base_key[i] * (x + y) * y)
            new_num = num
            while new_num > self.max_key_value:
                new_num = new_num - self.max_key_value
            num = abs(new_num)
            key.append(num)
            i += 1

        print("\n\nnew key")
        print(key)
        self.map_keys = key