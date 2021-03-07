# Simple LED color library
# By TBD1, TBD2, and Brygg Ullmer, Clemson University
# Begun 2021-03-07

import json, yaml
import sys, re
#import dotstar

############### Enodia LED color library ###############

class enLedColorLib:

  colorJsonFn   = 'colors1.json'
  colorHash     = {}
  basecolorsY   = '[blue,cyan,green,orange,purple,red,yellow]' #will extract first letter 
  basecolors    = None
  basecolorHash    = {}
  basecolorKeyHash = {}

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
    basecolors = yaml.load(self.basecolorsY)
    colorHashKeys = self.colorHash.keys()
    for basecolor in basecolors:
      self.basecolorHash[basecolor] = []
      basefirstletter = basecolor[0]
      self.basecolorKeyHash[basefirstletter] = basecolor

      for color in colorHashKeys:
        if re.search(basecolor, color, re.IGNORECASE):
          self.basecolorHash[basecolor].append(color)

    print(self.basecolorHash)

  ##################### constructor #####################

  def __init__(self):
    self.loadColorJson()
    self.extendColorHash()

def main():
  elcl = enLedColorLib()

if __name__ == "__main__":
  main()

### end ###
