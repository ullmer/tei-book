# Enodia Hex Plinth Simulator
# By Brygg Ullmer and TBD, Clemson University
# Begun 2021-04-11

# Resources:
# https://www.python-course.eu/tkinter_canvas.php

from tkinter import *

################# Enodia Hex Plinth GUI Simulator #################

class enHexPlinthSim():

  canvas_width    = 900
  canvas_height   = 450

  root            = None
  canvas          = None
  backgroundImg   = None
  backgroundImgFn = "images/enHexPlinthSim02b.png"

  def buildGui(self):

    self.root   = Tk()
    self.canvas = Canvas(root, width=canvas_width, height=canvas_height)
    self.canvas.pack()

    self.backgroundImg = PhotoImage(file=self.backgroundImgFn)
    canvas.create_image(0, self.canvas_height, anchor=NW, image=self.backgroundImg)

################# main #################

ehps = enHexPlinthSim()
mainloop()

### end ###

