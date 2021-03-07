###### Simple support code for TEI interaction ###### 
# By Millon McClelland, Brygg Ullmer, and TBD, Clemson University
# Begun 2021-03-07

from redYaKb import *
import sys

##################### support callback functions #####################

class rykTeiEx04(redYaKb):

  ##################### turn all LEDs red #####################
  def allRed(self):    
    self.selfDoc('pushLED')
    print('Millon, can you integrate the right calls here, please?')

  ##################### turn all LEDs red #####################
  def allGreen(self):  
    self.selfDoc('pushLED')

  ##################### turn all LEDs red #####################
  def allBlue(self):   
    self.selfDoc('pushLED')

  ##################### turn all LEDs red #####################
  def help(self):      
    self.selfDoc('pushLED')

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


### end ###
