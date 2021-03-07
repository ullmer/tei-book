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

  def pushLED:
    selfDoc('pushLED')

  def pullNFCs:
    selfDoc('pullNFCs')

  def describeHW:
    selfDoc('describeHW')

  def specPhysical:
    selfDoc('specPhysical')

  def specVirtual:
    selfDoc('specVirtual')

  def specTextual:
    selfDoc('specTextual')

  def wait1:
    selfDoc('wait1')

  def wait2:
    selfDoc('wait2')

  def wait3:
    selfDoc('wait3')

### end ###
