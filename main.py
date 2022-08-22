from Window_Class import Window
from Canvas_Class import Mod_Canvas
from Navigation_bar_Class import Nav_bar

root = Window()

canvas = Mod_Canvas(root, (255, 255, 255))
canvas.draw()
nav_bar = Nav_bar(root, canvas)
nav_bar.draw()


root.mainloop()

