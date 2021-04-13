###### Simple support code for TEI interaction ###### 
# By Brygg Ullmer, Millon McClelland, and TBD, Clemson University
# Begun 2021-03-07

#enLedColorLib (where Enodia is the name for an NSF MRI grant providing
#  relevant financial support) hopefully simplifies certain interactions
#  with strips of LEDs

from enLedColorLib import *
import sys, time

################## main ################

def main():
  elcl = enLedColorLib('neopixel')
  elcl.ledFill((1,1,3))

  #colorseqK = 'roygbpP'
  colorseqK = 'roygbp'
  colorseqH = elcl.getBasecolorSeq(colorseqK)
  print(colorseqH)
  for i in range(len(colorseqK)):
    ch = colorseqH[i]
    ct = elcl.mapColorIntensity(ch, '1') #0..F (and maybe Z)
    print(ch, ct)
    elcl.ledFill(ct)
    time.sleep(1)
  
  elcl.ledFill((0,0,0))
  for i in range(len(colorseqK)):
    ch = colorseqH[i]
    ct = elcl.mapColorIntensity(ch, '1') #0..F (and maybe Z)
    print(ch, ct)
    elcl.ledSet(ct, i)
    time.sleep(1)

if __name__ == "__main__":
  main()

### end ###
