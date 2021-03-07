# Simple LED color library
# By TBD1, TBD2, and Brygg Ullmer, Clemson University
# Begun 2021-03-07

import json
import sys
#import dotstar

############### Enodia LED color library ###############

class enLedColorLib:

  colorJsonFn = 'colors1.json'
  colorHash   = {}

############### load color json ###############

  def loadColorJson(self):
    jf = open(self.colorJsonFn, 'r+t')
    jd = json.load(jf)
    for color in jd:
      name = color['name']
      hex = color['hex']
      self.colorHash[name] = hex

### end ###
