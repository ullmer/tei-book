# Simple LED color library
# By TBD1, TBD2, and Brygg Ullmer, Clemson University
# Begun 2021-03-07

import json, yaml
import sys, re

############### Enodia LED color library ###############

class enLedColorLib:
  whichLedType = None
  pixels       = None #suggested neopixel handle

  colorJsonFn   = 'colors1.json'
  colorHash     = {}
  basecolorsY   = '[blue,cyan,green,orange,purple,red,yellow]' #will extract first letter 
  basecolors    = None
  basecolorHash    = None
  basecolorKeyHash = {}
  verbose       = False
  basecolorIdx  = {}

  ############### load color json ###############

  def loadColorJson(self):
    jf = open(self.colorJsonFn, 'r+t')
    jd = json.load(jf)
    for color in jd:
      name = color['name']
      hex = color['hex']
      self.colorHash[name] = hex

  ############### extend color hash ###############

  def extendColorHash(self): 
    self.basecolorHash = {}
    basecolors = yaml.load(self.basecolorsY)
    colorHashKeys = self.colorHash.keys()
    for basecolor in basecolors:
      self.basecolorHash[basecolor] = []
      basefirstletter = basecolor[0]
      self.basecolorKeyHash[basefirstletter] = basecolor
      self.basecolorIdx[basecolor] = 0 # default to first basecolor match in colors.json

      for color in colorHashKeys:
        if re.search(basecolor, color, re.IGNORECASE):
          self.basecolorHash[basecolor].append(color)

      if self.verbose:
        print(basecolor, self.basecolorHash[basecolor])
  
  ############### get basecolor sequence ###############

  def getBasecolorSeq(self, colorseq):  #colorseq example: oopoop for (orange-orange-purple)x2
    if self.basecolorHash == None:
      print("enLedColorLib getBasecolorSeq error: basecolorHash is none!")
      return(False)

    colorseqLen = len(colorseq)
    result = []
    for seqidx in range(colorseqLen):
      try:
        basecolorKey = colorseq[seqidx]
        basecolor    = self.basecolorKeyHash[basecolorKey]
        basecoloridx = self.basecolorIdx[basecolor]
        color        = self.basecolorHash[basecolor][basecoloridx]
        colorhex     = self.colorHash[color]
        result.append(colorhex)
      except:
        print("enLedColorLib getBasecolorSeq problem:")
        e = sys.exc_info()   #e = sys.exc_info()[0]
        print('error: '+str(e))
        return False

    return result
  
  ############### led fill ###############

  def ledFill(self, colorDescr):  
    if self.whichLedType == 'neopixel': self.pixels.fill(colorDescr)

  ############### led set ###############

  def ledSet(self, colorDescr, whichLed):  
    if self.whichLedType == 'neopixel': self.pixels[whichLed] = colorDescr

  ############### led Array ###############

  def ledArray(self, colorDescrList):  
    if self.whichLedType == 'neopixel': 
      for i in range(len(colorDescrList)):
        c = colorDescrList[i]
        self.ledSet(c, i)

  ############### map color intensity###############

  def mapColorIntensity(self, colorHex, intensityHex):  #colorseq example: oopoop for (orange-orange-purple)x2
    #colorHex example: #C46210
    try:
      colorTuple = tuple(int(colorHex[i:i+2], 16) for i in (1, 3, 5)) 
      #https://stackoverflow.com/questions/29643352/converting-hex-to-rgb-value-in-python/29643643
    except:
      print("enLedColorLib mapColorIntensity problem converting color hexstring:")
      e = sys.exc_info()   #e = sys.exc_info()[0]
      print('error: '+str(e))
      return False

    if not isinstance(intensityHex,str) or len(intensityHex) != 1:
      print("enLedColorLib mapColorIntensity problem: intensityHex must be a single-character string"); return False

    try:
      intensityInt = int(intensityHex[0:1], 16)
    except:
      print("enLedColorLib mapColorIntensity problem converting intensityHex")
      e = sys.exc_info(); print('error: '+str(e)); return False

    #intensity = float(intensityInt)/10.
    #intensity = float(intensityInt)/15.
    intensity = float(intensityInt)/64.
    result = tuple(int(float(colorTuple[i] * intensity)) for i in range(3))
    #print(colorHex)
    #print(colorTuple)
    #print(intensityInt)
    #print(result)
    return result

  ############### get basecolor sequence ###############

  def mapSeqIntensity(self, colorHexSeq, intensityHexSeq):  #colorseq example: oopoop for (orange-orange-purple)x2

    if not isinstance(intensityHexSeq,str):
      print("enLedColorLib mapSeqIntensity: argument intensityHexSeq must be a string"); return False

    ihsLen = len(intensityHexSeq)

    scaledColors = []
    for i in range(ihsLen):
      scaledColor = self.mapColorIntensity(colorHexSeq[i], intensityHexSeq[i])
      scaledColors.append(scaledColor)
      
    return scaledColors

  ##################### constructor #####################

  def __init__(self, whichLedType=None):
    self.loadColorJson()
    self.extendColorHash()
    self.whichLedType = whichLedType

    if self.whichLedType == 'dotstar': import dotstar
    if self.whichLedType == 'neopixel':
      import board
      import neopixel
      self.pixels = neopixel.NeoPixel(board.D18, 12)

def main():
  elcl = enLedColorLib()
  print(elcl.basecolorKeyHash.keys())
  colorseq = elcl.getBasecolorSeq('oopoop')
  print(colorseq)
  scaledColor = elcl.mapSeqIntensity(colorseq, 'A9BAAA')
  print(colorseq[0], scaledColor)

if __name__ == "__main__":
  main()

### end ###
