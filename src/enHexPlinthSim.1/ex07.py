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

if __name__ == "__main__":
  main()

### end ###
