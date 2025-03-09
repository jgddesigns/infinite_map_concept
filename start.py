from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

from classes.Main import Main




class InfiniteMap(App):
    size_multiplier = 1.5
    default_width = 800 
    default_height = 450 * size_multiplier

    key = None
    draw = None
    position = None
    player = None
    main = None




    Builder.load_file("main.kv")




    def build(self):
        try:
            Window.size = (self.default_width, self.default_height)

            self.main = Main()
            self.main.start()
                    
            return self.main
        
        except Exception as e:
            print("\n\nError in 'InfiniteMap' Class - 'build' Function", e)   




if __name__ == "__main__":
    InfiniteMap().run()


