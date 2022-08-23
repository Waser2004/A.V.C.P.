from Canvas_Class import Mod_Canvas
from Window_Class import Window
from tkinter import W
import math


class Nav_bar(object):
    def __init__(self, root: Window, canvas: Mod_Canvas):
        self.win = root
        self.canvas = canvas.canvas

        self.active_page = 0
        self.page_list = ["Home", "Storage", "Create new"]

        self.background_label = None
        self.page_label = [None, None, None]

    def draw(self):
        if self.background_label is None:
            color = self.rgb(87, 112, 230)
            self.background_label = self.canvas.create_rectangle(0, 0, self.win.win_size[0] + 10, 50, fill=color, outline=color)

        for i, txt in enumerate(self.page_list):
            if self.page_label[i] is None:
                self.page_label[i] = self.canvas.create_text(25+100*i, 25, anchor=W, text=txt, fill="white", font=("Arial", 15))

    @staticmethod
    def rgb(r: int, g: int, b: int) -> str:
        assert -1 < r < 256 and -1 < g < 256 and -1 < b < 256, "All rgb values have to be between 0 and 255"

        out = "#"
        hex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "b", "c", "d", "e", "f"]

        out += f"{hex_list[math.floor(r/16)]}{hex_list[round((r/16-math.floor(r/16))*16)]}"
        out += f"{hex_list[math.floor(g/16)]}{hex_list[round((g/16-math.floor(g/16))*16)]}"
        out += f"{hex_list[math.floor(b/16)]}{hex_list[round((b/16-math.floor(b/16))*16)]}"

        return out


