from Window_Class import Window
from Navigation_bar_Class import Nav_bar
from Canvas_Class import Mod_Canvas


class Event_Manager(object):
    def __init__(self, root: Window, nav_bar: Nav_bar, canvas: Mod_Canvas):
        self.root = root
        self.nav_bar = nav_bar
        self.canvas = canvas

    def Button_1(self, event):
        self.nav_bar.mouse_left_click(event)

    def window_resize(self, event):
        self.canvas.resize()
        self.nav_bar.resize()

