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
  commandHash      = None

  ##################### constructor ##################### 

  def __init__(self, commandsYamlFn):
    self.ingestCommandYamlFn(commandsYamlFn)
    self.listCommands()

  ##################### help ##################### 

  def help(self):
    print("redYaKb help stub")

  ##################### help ##################### 

  def selfDoc(self, selfCmd):
    print("self documentation called for command " + selfCmd)

  ##################### read + process file containing yaml command bindings #####################

  def ingestCommandYamlFn(self, sourceYamlFn): 
    try:
      yf = open(sourceYamlFn, 'r+t')
    except:
      print("redYaKab ingestCommandYaml: problem opening file " + sourceYamlFn) 
      e = sys.exc_info()   #e = sys.exc_info()[0]
      print('error: '+str(e))
      return False

    self.yamlCommandDescr = yaml.safe_load(yf)

    numCommands = len(self.yamlCommandDescr)
    print("redYaKb ingestCommandYamlFn processing " + str(numCommands) + " commands from file " + sourceYamlFn)

    self.commandHash = {}
    for commandDescr in self.yamlCommandDescr:
      if 'key' in commandDescr:
        key = commandDescr['key']
        self.commandHash[key] = commandDescr
        cmd = self.getCmd(commandDescr)
      else:
        print("redYaKab ingestCommandYaml: problem parsing command entry: " + commandDescr)

    #return result
    return True

  ##################### list commands ##################### 

  def getCmd(self, commandDescr):
    if 'command' in commandDescr:
      commandTxt = commandDescr['command']
      try:
        attr = getattr(self, commandTxt)
        return attr
      except:
        print("redYaKab getCmd: problem with getattr " + commandTxt) 
        e = sys.exc_info()   #e = sys.exc_info()[0]
        print('error: '+str(e))
        return False
    else:
      print("redYaKab getCmd: 'command' not found in commandDescr: " + commandDescr)
      return False

  ##################### list commands ##################### 

  def listCommands(self): 
    if self.commandHash == None:
      print("redYaKab listCommands: commandHash is null (ingestCommandYamlFn likely not called)")
      return False

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
