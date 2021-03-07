###### Simple support code for TEI interaction supported by redis ###### 
# Brygg Ullmer (Clemson U.) and xxx
# Begun 2021-03-05

import redis 
import yaml
import getch

##################### redis yaml keyboard class #####################

class redYaKb:

  ##################### read character w/o newline #####################

  def readCh(self): # (blocking)
    result = getch.getch()
    return result

  ##################### process character #####################

  def procCh(self, ch=None): #if none, will use readCh (blocking)
    if ch == None:
      ch = self.readCh()

    print(">>> " + ch)

#### end ###
