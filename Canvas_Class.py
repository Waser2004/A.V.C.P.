import math
from tkinter import Canvas
from Window_Class import Window


class Mod_Canvas(object):
    def __init__(self, root: Window, background: (int, int, int) = (0, 0, 0)):
        self.win = root
        self.canvas = Canvas(self.win.win, bg=self.rgb_to_hex(background[0], background[1], background[2]))

    def draw(self):
        self.canvas.place(x=-2, y=-2, width=self.win.win_size[0]+10, height=self.win.win_size[1]+10)

    @staticmethod
    def rgb_to_hex(r: int, g: int, b: int) -> str:
        assert -1 < r < 256 and -1 < g < 256 and -1 < b < 256, "All rgb values have to be between 0 and 255"

        out = "#"
        hex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "b", "c", "d", "e", "f"]

        out += f"{hex_list[math.floor(r/16)]}{hex_list[round((r/16-math.floor(r/16))*16)]}"
        out += f"{hex_list[math.floor(g/16)]}{hex_list[round((g/16-math.floor(g/16))*16)]}"
        out += f"{hex_list[math.floor(b/16)]}{hex_list[round((b/16-math.floor(b/16))*16)]}"

        return out
