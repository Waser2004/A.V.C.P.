from Window_Class import Window
from Canvas_Class import Mod_Canvas
from Navigation_bar_Class import Nav_bar
from Event_Manager_class import Event_Manager


root = Window()

canvas = Mod_Canvas(root, (255, 255, 255))
nav_bar = Nav_bar(root, canvas)

ev = Event_Manager(nav_bar)

canvas.draw()
nav_bar.draw()

root.win.bind("<Button-1>", ev.Button_1)


root.mainloop()



