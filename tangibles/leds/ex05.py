###### Simple support code for TEI interaction ###### 
# By Millon McClelland, Brygg Ullmer, and TBD, Clemson University
# Begun 2021-03-07

from redYaKb import *
from enLedColorLib import *
import sys

############################################################## 
################## support callback functions ################

class rykEx05(redYaKb):

  ##################### turn all LEDs red #####################
  def allRed(self):    
    self.selfDoc('allRed')
    print('Millon, can you integrate the right calls here, please?')

  ##################### turn all LEDs red #####################
  def allGreen(self):  
    self.selfDoc('allGreen')
    print('Millon, can you integrate the right calls here, please?')

  ##################### turn all LEDs red #####################
  def allBlue(self):   
    self.selfDoc('allBlue')
    print('Millon, can you integrate the right calls here, please?')

  ##################### turn all LEDs red #####################
  def wait1(self):     
    self.selfDoc('wait1')
    sys.sleep(1)

  ##################### turn all LEDs red #####################
  def wait2(self):     
    self.selfDoc('wait1')
    sys.sleep(2)

  ##################### turn all LEDs red #####################
  def wait3(self):     
    self.selfDoc('wait1')
    sys.sleep(3)

############################################################## 
################## support callback functions ################

def main():
  elcl = enLedColorLib()
  print(elcl.basecolorKeyHash.keys())
  colorseq = elcl.getBasecolorSeq('oopoop')
  print(colorseq)
  scaledColor = elcl.mapSeqIntensity(colorseq, 'A9BAAA')
  print(colorseq[0], scaledColor)

  cyfn = 'ex05.yaml' #commands yaml filename
  ryk = rykEx05(cyfn)

  print('Entering blocking keyboard loop.  Press "h" for help=list of commands.')

  while True:
    ryk.procCh()

if __name__ == "__main__":
  main()

### end ###

### end ###
