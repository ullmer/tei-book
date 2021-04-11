# Enodia Hex Plinth Simulator
# By Brygg Ullmer and TBD, Clemson University
# Begun 2021-04-11

# Resources:
# https://www.python-course.eu/tkinter_canvas.php

from tkinter import *

################# Enodia Hex Plinth GUI Simulator #################

class enHexPlinthSim():

  canvas_width  = 900
  canvas_height = 450

  root          = None
  canvas        = None
  bgImg         = None #background image
  bgImgFn       = "images/enHexPlinthSim02b.png"

  def buildGui(self):

    self.root   = Tk()
    self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
    self.canvas.pack()

    self.bgImg = PhotoImage(file=self.bgImgFn)
    #self.canvas.create_image(0, self.canvas_height, anchor=NW, image=self.bgImg)
    self.canvas.create_image(0, 0, anchor=NW, image=self.bgImg)

################# main #################

ehps = enHexPlinthSim()
ehps.buildGui()
mainloop()

### end ###

