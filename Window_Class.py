from tkinter import Tk


class Window(object):
    def __init__(self, window_size: (int, int) = (1120, 630)):
        self.win = Tk()
        self.win.geometry(f"{window_size[0]}x{window_size[1]}")
        self.win.update()

    def mainloop(self):
        self.win.mainloop()

