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
        print("redYaKb ingestCommandYaml: problem opening file " + sourceYamlFn) 
        e = sys.exc_info()   #e = sys.exc_info()[0]
        print('error: '+str(e))
        return False

    return result

  ##################### constructor #####################

  def __init__(self):
    self.loadColorJson()
    self.extendColorHash()

def main():
  elcl = enLedColorLib()
  print(elcl.basecolorKeyHash.keys())
  print(elcl.getBasecolorSeq('oopoop'))

if __name__ == "__main__":
  main()

### end ###
