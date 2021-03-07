###### Simple support code for TEI interaction supported by redis ###### 
# Brygg Ullmer (Clemson U.) and xxx
# Begun 2021-03-05

import redis 
import yaml
import getch
import sys

##################### redis yaml keyboard class #####################

class redYaKb:

  yamlCommandDescr = None

  ##################### constructor ##################### 

  def __init__(self, commandsYamlFn):
    self.ingestCommandYamlFn(commandsYamlFn)

  ##################### read + process file containing yaml command bindings #####################

  def ingestCommandYamlFn(self, sourceYamlFn): 
    try:
      yf = open(sourceYamlFn, 'r+t')
    except:
      print("redYaKab: problem opening file " + sourceYamlFn) 
      e = sys.exc_info()   #e = sys.exc_info()[0]
      print('error: '+str(e))
      return False

    self.yamlCommandDescr = yaml.safe_load(yf)

    numCommands = len(self.yamlCommandDescr)
    print("redYaKb ingestCommandYamlFn processing " + str(numCommands) + " commands from file " + sourceYamlFn)
    
    #return result
    return True

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
