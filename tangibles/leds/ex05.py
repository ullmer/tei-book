###### Simple support code for TEI interaction ###### 
# By Brygg Ullmer, Millon McClelland, and TBD, Clemson University
# Begun 2021-03-07

#Two provided support libraries are engaged.  

#redYaKb integrates Redis, Yaml, and getch (keyboard) functionalities
#  While the redis functionality isn't engaged by the following, it is 
#  likely to become important toward a number of behaviors

#enLedColorLib (where Enodia is the name for an NSF MRI grant providing
#  relevant financial support) hopefully simplifies certain interactions
#  with strips of LEDs

from redYaKb import * 
from enLedColorLib import *
import sys

############################################################## 
################## support callback functions ################

class rykEx05(redYaKb):
  numLeds  = 13 #6  # This number should be set per whatever strip(s) are used
  colorlib = None

  ##################### constructor #####################

  def __init__(self, commandsYamlFn):
    self.ingestCommandYamlFn(commandsYamlFn)
    self.listCommands()
    self.colorlib = enLedColorLib()
  
  ##################### simple color functions #####################

  def genColorSeq(self, colorKey, intensity=10):

    #here, "colorKey" is a single letter like o(range), p(urple), etc.; and
    #intensity is an integer, where 10 = "full intensity"; 1="10% intensity"; etc.
    # values above 15 are currently wrapped back to 15

    colorkeyseq  = colorKey * self.numLeds #generate a sequence of numLeds characters
    intensityseq = 'A' * self.numLeds  #default to nominal 100% intensity

    colorseq       = self.colorlib.getBasecolorseq(colorkeyseq)
    scaledColorseq = self.colorlib.mapSeqIntensity(colorseq, intensityseq)
    return scaledColorseq

  def ledAllOneColor(self, colorkey):
    self.selfDoc('allRed called')
    colorseq = self.genColorSeq(colorkey)
    self.colorlib.lightLedStrip(colorseq)

  def ledAllOff(self):
    self.selfDoc('allRed called')
    colorseq = []
    for led in range(self.numLeds):
      colorseq.append(tuple(0,0,0))

    self.colorlib.lightLedStrip(colorseq)

  ##################### simple color functions #####################

  def allRed(self):    
    self.selfDoc('allRed called')
    self.ledAllOneColor('r')

  def allGreen(self):  
    self.selfDoc('allGreen')
    self.ledAllOneColor('g')

  def allBlue(self):   
    self.selfDoc('allBlue')
    self.ledAllOneColor('b')

  def allOrange(self):   
    self.selfDoc('allOrange')
    self.ledAllOneColor('o')

  def allPurple(self):   
    self.selfDoc('allPurple')
    self.ledAllOneColor('p')

  def allBlack(self):   
    self.selfDoc('allPurple')
    self.ledAllOff()

  ##################### wait functions #####################
  def wait1(self):     
    self.selfDoc('wait1')
    sys.sleep(1)

  def wait2(self):     
    self.selfDoc('wait1')
    sys.sleep(2)

  def wait3(self):     
    self.selfDoc('wait1')
    sys.sleep(3)

############################################################## 
################## support callback functions ################

def main():
  elcl = enLedColorLib()
  #print(elcl.basecolorKeyHash.keys())
  colorseq = elcl.getBasecolorSeq('oopoop')
  #print(colorseq)
  scaledColor = elcl.mapSeqIntensity(colorseq, 'A9BAAA')
  #print(colorseq[0], scaledColor)

  cyfn = 'ex05.yaml' #commands yaml filename
  ryk = rykEx05(cyfn)

  print('Entering blocking keyboard loop.  Press "h" for help=list of commands.')

  while True:
    ryk.procCh()

if __name__ == "__main__":
  main()

### end ###
