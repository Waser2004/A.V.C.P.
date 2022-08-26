from Navigation_bar_Class import Nav_bar


class Event_Manager(object):
    def __init__(self, nav_bar: Nav_bar):
        self.nav_bar = nav_bar

    def Button_1(self, event):
        self.nav_bar.mouse_left_click(event)