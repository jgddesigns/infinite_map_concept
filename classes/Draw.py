from random import randint
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line, Rectangle, Ellipse, Color

class Draw(Widget):
    base_size = (20, 20)
    positions = []




    def __init__(self, **kwargs):
        super().__init__(**kwargs)




    def draw_shapes(self):
        try:
            self.canvas.clear()
            self.positions = []
            with self.canvas:
                for key in App.get_running_app().main.key.map_keys:
                    self.get_color(key)  
                    self.get_shape(key)  

        except Exception as e:
            print("\n\nError in 'Draw' Class - 'draw_shapes' Function", e)

    
    def get_shape(self, key):
        try:
            if int(str(key)[len(str(key))-1]) <= 2:
                self.rectangle(key)
            elif int(str(key)[len(str(key))-1]) > 2 and int(str(key)[len(str(key))-1]) <= 5:
                self.circle(key)
            elif int(str(key)[len(str(key))-1]) > 6 and int(str(key)[len(str(key))-1]) <= 6:
                self.circle(key)
            elif int(str(key)[len(str(key))-1]) == 7:
                self.rectangle(key)
            elif int(str(key)[len(str(key))-1]) == 8:
                self.oval(key)
            elif int(str(key)[len(str(key))-1]) == 9:
                self.pentagon(key)

        except Exception as e:
            print("\n\nError in 'Draw' Class - 'get_shape' Function", e)             


    def get_color(self, key):
        try:
            try:
                if int(str(key)[len(str(key))-2]) <= 1:
                    Color(*(1, 0, 0, 1))
                elif int(str(key)[len(str(key))-2]) == 2:
                    Color(*(0, 1, 0, 1))
                elif int(str(key)[len(str(key))-2]) == 3:
                    Color(*(0, 0, 1, 1))
                elif int(str(key)[len(str(key))-2]) == 4:
                    Color(*(1, 1, 0, 1))
                elif int(str(key)[len(str(key))-2]) == 5:
                    Color(*(0, 1, 1, 1))
                elif int(str(key)[len(str(key))-2]) == 6:
                    Color(*(1, 0, 1, 1))
                elif int(str(key)[len(str(key))-2]) == 7:
                    Color(*(0, 0.5, 0, 1))
                elif int(str(key)[len(str(key))-2]) == 8:
                    Color(*(0.5, 0.5, 1, 1))
                elif int(str(key)[len(str(key))-2]) == 9:
                    Color(*(0.5, 0, 0.5, 1))
            except: 
                Color(*(1, 0, 0, 1))

        except Exception as e:
            print("\n\nError in 'Draw' Class - 'get_color' Function", e) 

    
    def get_position(self, key, position=None):
        try:
            try:
                hundreds = int(str(key)[0])
            except:
                hundreds = 1

            try: 
                tens = int(str(key)[1])
            except:
                tens = 1

            try:
                ones = int(str(key)[2])
            except:
                ones = 1

            if position == None:
                position = [abs((hundreds + tens) * ones) * 8, abs((ones + tens) * hundreds) * 6]

            if len(self.positions) > 0:
                for existing in self.positions:
                    if abs(position[0] - existing[0]) <= self.base_size[0] or abs(position[1] - existing[1]) <= self.base_size[0]:
                        position[0] = position[0] + 1
                        position[1] = position[1] + 1

                        return self.get_position(key, position)

            if position not in self.positions:        
                self.positions.append(position)
                return position
            
            else:
                return self.get_position(key, position)
            
        except Exception as e:
            print("\n\nError in 'Draw' Class - 'get_position' Function", e) 


    def rectangle(self, key):
        try:
            Rectangle(pos=self.get_position(key), size=self.base_size)

        except Exception as e:
            print("\n\nError in 'Draw' Class - 'rectangle' Function", e) 


    def circle(self, key):
        try:
            Ellipse(pos=self.get_position(key), size=self.base_size)

        except Exception as e:
            print("\n\nError in 'Draw' Class - 'circle' Function", e) 


    def star(self, key):
        try:
            pos = self.get_position(key)
            points = [
                pos[0] + 20, pos[1] + 60, 
                pos[0] + 80, pos[1] + 60, 
                pos[0] + 30, pos[1] + 100,
                pos[0] + 50, pos[1] + 160, 
                pos[0], pos[1] + 120, 
                pos[0] - 50, pos[1] + 160, 
                pos[0] - 30, pos[1] + 100,
                pos[0] - 80, pos[1] + 60, 
                pos[0] - 20, pos[1] + 60, 
                pos[0], pos[1]
            ]
            Line(points=points, width=2)

        except Exception as e:
            print("\n\nError in 'Draw' Class - 'star' Function", e) 
            

    def oval(self, key):
        try:
            Ellipse(pos=self.get_position(key), size=(self.base_size[0], self.base_size[0]/2))

        except Exception as e:
            print("\n\nError in 'Draw' Class - 'oval' Function", e) 


    def pentagon(self, key):
        try:
            pos = self.get_position(key)
            points = [
                pos[0] + self.base_size[0]/4, pos[1] + self.base_size[0]/2,
                pos[0], pos[1] + self.base_size[0],
                pos[0] - self.base_size[0]/2, pos[1] + self.base_size[0],
                pos[0] - self.base_size[0] * .75, pos[1] + self.base_size[0]/2,
            ]
            Line(points=points, close=True)

        except Exception as e:
            print("\n\nError in 'Draw' Class - 'pentagon' Function", e) 