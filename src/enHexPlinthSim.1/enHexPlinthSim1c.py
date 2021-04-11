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
  fxmax         = 6.
  fymax         = 3.

  ledSimFXY1    = (.065, .05) #F = floating-point, per integer units of CDR
  ledSimFXY2    = (.265, .25)
  ledSimFdX     = .25
  ledSimSXY1    = None        #S = screen/integer pixel coords
  ledSimSXY2    = None        #S = screen/integer pixel coords

  root          = None
  canvas        = None
  bgImg         = None #background image
  bgImgFn       = "images/enHexPlinthSim02b.png"

  ledSimMap     = None

################# constructor #################
  def __init__(self):
    self.ledSimMap = []
    self.mapScreenCoords(self): 

################# mapCoord #################
  def mapCoord(self, fx, fy): #fx, fy are floating-point coords, per CDR sketch
    fxRel = float(fx) / self.fxmax
    fyRel = float(fy) / self.fymax
    x     = int(fxRel * self.fxmax)
    y     = int(fyRel * self.fymax)
    return (x,y) 

################# mapCoord #################
  def mapScreenCoords(self): 
    xy1 = self.ledSimFXY1
    xy2 = self.ledSimFXY2
    self.ledSimSXY1 = self.mapCoord(xy1[0], xy1[1])
    self.ledSimSXY2 = self.mapCoord(xy2[0], xy2[1])

################# build gui #################
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

