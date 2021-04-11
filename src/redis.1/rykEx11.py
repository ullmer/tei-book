###### Simple support code for TEI interaction ###### 
# By Brygg Ullmer and TBD, Clemson University
# Begun 2021-03-07

from redYaKb import *
import sys

##################### support callback functions #####################

class rykEx11(redYaKb):

  ##################### turn all LEDs red #####################
  def allRed(self):    
    self.selfDoc('allRed')

  ##################### turn all LEDs red #####################
  def allGreen(self):  
    self.selfDoc('allGreen')

  ##################### turn all LEDs red #####################
  def allBlue(self):   
    self.selfDoc('allBlue')

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
