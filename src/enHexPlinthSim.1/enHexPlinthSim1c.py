# Enodia Hex Plinth Simulator
# By Brygg Ullmer and TBD, Clemson University
# Begun 2021-04-11

# Resources:
# https://www.python-course.eu/tkinter_canvas.php

from   tkinter import *
import yaml

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
  bgImgFn       = "images/enHexPlinthSim02d.png"
  ledLinesY     = '''{1: [.33,1.3,.606,1.775],    2: [.33,1.179,.606,.704], 
                      3: [.71,.645,1.259,.645],   4: [1.363,.704,1.637,1.179],
                      5: [1.637,1.3,1.363,1.775], 6: [1.259,1.834,.71,1.834]}'''
  ledLinesF     = None
  ledLinesS     = None
  ledLinesHash  = None
  ledLineWidth  = 10

  numSimLeds      = 12
  ledSimHash      = None
  ledSimBaseColor = "#808080"

################# constructor #################
  def __init__(self):
    self.ledSimHash = {}
    self.initScreenCoords()

################# mapCoord #################
  def mapCoord(self, fx, fy): #fx, fy are floating-point coords, per CDR sketch
    fxRel = float(fx) / self.fxmax
    fyRel = float(fy) / self.fymax
    x     = int(fxRel * self.canvas_width)
    y     = self.canvas_height - int(fyRel * self.canvas_height)
    return (x,y) 

################# initialize screen coordinates #################
  def initScreenCoords(self): 
    xy1 = self.ledSimFXY1
    xy2 = self.ledSimFXY2
    self.ledSimSXY1 = self.mapCoord(xy1[0], xy1[1])
    self.ledSimSXY2 = self.mapCoord(xy2[0], xy2[1])

    self.ledLinesF = {}; self.ledLinesS = {}; self.ledLinesHash = {}
    self.ledLinesD = yaml.safe_load(self.ledLinesY)
    for key in self.ledLinesD.keys():
      linesF = self.ledLinesD[key]
      coord1 = self.mapCoord(linesF[0], linesF[1])
      coord2 = self.mapCoord(linesF[2], linesF[3])
      self.ledLinesS[key] = [coord1, coord2]

################# draw hex lines #################
  def drawHexLines(self): 
    for key in self.ledLinesS.keys():
      lineS = self.ledLinesS[key]          #line description in screen-coordinates
      v1 = lineS[0]; v2 = lineS[1] #the vertices
      self.ledLinesHash[key] = self.canvas.create_line(v1[0], v1[1], v2[0], v2[1],
        width=self.ledLineWidth, fill=self.ledSimBaseColor, capstyle=ROUND)

################# change simulated LED color #################
  def changeLEDSimColor(self, whichEl, whichColor):
    if whichEl not in self.ledSimHash:
      print("enHexPlinthSim changeLEDSimColor: index not found:", whichEl); return

    ledBoxHandle = self.ledSimHash[whichEl]

################# build LED simulator box #################
  def buildLEDSimBox(self, whichEl):
    b1 = self.ledSimSXY1
    b2 = self.ledSimSXY2
    dx = int(whichEl * float(self.canvas_width) * (self.ledSimFdX / self.fxmax))
    if b1 == None or b2 == None:
      print("enHexPlinthSim buildLEDSimBox error: ledSimSXY* are None"); return

    b1x = b1[0]+dx
    b2x = b2[0]+dx
    #print(str(dx) + str(b1) + str(b2) + str(b1x),str(b2x))

    r = self.canvas.create_rectangle(b1x, b1[1], b2x, b2[1], 
      fill=self.ledSimBaseColor)

    self.ledSimHash[whichEl] = r

################# build gui #################
  def buildGui(self):

    self.root   = Tk()
    self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
    self.canvas.pack()

    self.bgImg = PhotoImage(file=self.bgImgFn)
    self.canvas.create_image(0, 0, anchor=NW, image=self.bgImg)

    for i in range(self.numSimLeds):
      self.buildLEDSimBox(i)

    self.drawHexLines()

################# main #################

ehps = enHexPlinthSim()
ehps.buildGui()
mainloop()

### end ###

