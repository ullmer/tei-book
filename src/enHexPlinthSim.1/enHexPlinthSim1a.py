# Enodia Hex Plinth Simulator
# By Brygg Ullmer and TBD, Clemson University
# Begun 2021-04-11

# Resources:
# https://www.python-course.eu/tkinter_canvas.php

from tkinter import *

canvas_width  = 900
canvas_height = 450

root   = Tk()
canvas = Canvas(root, width=canvas_width, height=canvas_height)
canvas.pack()

img = PhotoImage(file="images/enHexPlinthSim02b.png")
#canvas.create_image(0, canvas_height, anchor=NW, image=img)
canvas.create_image(0, 0, anchor=NW, image=img)

mainloop()

### end ###

