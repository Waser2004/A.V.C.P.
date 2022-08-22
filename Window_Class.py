from tkinter import Tk


class Window(object):
    def __init__(self, window_size: (int, int) = (1120, 630)):
        self.win_size = [window_size[0], window_size[1]]

        self.win = Tk()
        self.win.geometry(f"{self.win_size[0]}x{self.win_size[1]}")

    def mainloop(self):
        self.win.mainloop()

