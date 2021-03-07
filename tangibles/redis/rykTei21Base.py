###### Simple support code for TEI interaction supported by redis ###### 
# Brygg Ullmer (Clemson U.) and xxx
# Begun 2021-03-05

import redis 
import yaml
import getch
import sys
import redYaKb

##################### redis yaml keyboard class #####################

class rykTei21Base(redYaKb):

  def pushLED(self):
    self.selfDoc('pushLED')

  def pullNFCs(self):
    self.selfDoc('pullNFCs')

  def describeHW(self):
    self.selfDoc('describeHW')

  def specPhysical(self):
    self.selfDoc('specPhysical')

  def specVirtual(self):
    self.selfDoc('specVirtual')

  def specTextual(self):
    self.selfDoc('specTextual')

  def wait1(self):
    self.selfDoc('wait1')

  def wait2(self):
    self.selfDoc('wait2')

  def wait3(self):
    self.selfDoc('wait3')

### end ###
