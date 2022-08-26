from Canvas_Class import Mod_Canvas
from Window_Class import Window
from Animation_class import Animation
from tkinter import W
from tkinter.font import Font
import math


class Nav_bar(object):
    def __init__(self, root: Window, canvas: Mod_Canvas):
        self.win = root
        self.canvas = canvas.canvas

        self.active_page = 0
        self.page_list = ["Home", "Storage", "Create new"]
        self.Link_font = Font(font=("Arial", 15))

        self.background_label = None
        self.page_label = [None, None, None]
        self.indicator_label = None

        self.indicator_x_animation = Animation()
        self.indicator_width_animation = Animation()

    def draw(self):
        # background
        if self.background_label is None:
            color = self.rgb(87, 112, 230)
            self.background_label = self.canvas.create_rectangle(0, 0, self.win.win.winfo_width()+10, 50, fill=color, outline=color)

        # links
        length = 0
        for i, txt in enumerate(self.page_list):
            if self.page_label[i] is None:
                self.page_label[i] = self.canvas.create_text(30+30*i+length, 25, anchor=W, text=txt, fill="white", font=("Arial", 15))
                length += self.Link_font.measure(txt)

        # position indicator
        if self.indicator_label is None:
            x = sum([self.Link_font.measure(txt) for txt in self.page_list[0:self.active_page]])+30*self.active_page+15
            width = self.Link_font.measure(self.page_list[self.active_page])+30
            self.indicator_label = self.canvas.create_rectangle(x, 48, x+width, 49, fill="white", outline="white")

        if self.indicator_x_animation.state is True or self.indicator_width_animation.state is True:
            self.canvas.delete(self.indicator_label)
            x, width = self.indicator_x_animation.step(), self.indicator_width_animation.step()
            self.indicator_label = self.canvas.create_rectangle(x, 48, x+width, 49, fill="white", outline="white")

    def mouse_left_click(self, event):
        if event.y <= 50:
            x = event.x-15
            for i, txt in enumerate(self.page_list):
                x -= 30+self.Link_font.measure(txt)
                if x < 0:
                    self.animate_indicator(self.active_page, i)
                    self.active_page = i
                    break

    def animate_indicator(self, cur_active: int, tar_active: int):
        x_1 = sum([self.Link_font.measure(txt) for txt in self.page_list[0:cur_active]])+30*cur_active+15
        x_2 = sum([self.Link_font.measure(txt) for txt in self.page_list[0:tar_active]])+30*tar_active+15
        self.indicator_x_animation.animate(x_1, x_2, 10)

        width_1 = self.Link_font.measure(self.page_list[cur_active])+30
        width_2 = self.Link_font.measure(self.page_list[tar_active])+30
        self.indicator_width_animation.animate(width_1, width_2, 10)

    def resize(self):
        self.clear()
        self.draw()

    def clear(self):
        self.canvas.delete(self.background_label)
        self.background_label = None

        for x in self.page_label:
            self.canvas.delete(x)
        self.page_label = [None, None, None]

        self.canvas.delete(self.indicator_label)
        self.indicator_label = None


    @staticmethod
    def rgb(r: int, g: int, b: int) -> str:
        assert -1 < r < 256 and -1 < g < 256 and -1 < b < 256, "All rgb values have to be between 0 and 255"

        out = "#"
        hex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "b", "c", "d", "e", "f"]

        out += f"{hex_list[math.floor(r/16)]}{hex_list[round((r/16-math.floor(r/16))*16)]}"
        out += f"{hex_list[math.floor(g/16)]}{hex_list[round((g/16-math.floor(g/16))*16)]}"
        out += f"{hex_list[math.floor(b/16)]}{hex_list[round((b/16-math.floor(b/16))*16)]}"

        return out


