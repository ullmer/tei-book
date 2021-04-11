###### Simple support code for TEI interaction supported by redis ###### 
# Brygg Ullmer (Clemson U.) and xxx
# Begun 2021-03-05


# https://pypi.org/project/pynput/
# https://stackoverflow.com/questions/53088995/pynput-keyboard-listener-does-not-detect-keys-on-mac-os-x
# on Mac, one must go to System Preferences -> Security and Privacy -> Privacy -> 
# Accessibility, and add "Terminal" to "Allow the apps below to control your 
# computer" (if you are running Python or Python3 from Terminal)

import sys
import yaml
import redis 
import asyncio
import aioredis 

from pynput import keyboard

# python3 -m pip install redis pyyaml pynput

##################### redis yaml keyboard class #####################

class redYaKb:

  yamlCommandDescr = None
  commandHash      = None
  kbListener       = None

  host = "redis-15905.c56.east-us.azure.cloud.redislabs.com"
  port = "15905"
  pw   = None
  pool       = None  #redis handle
  receiver   = None
  channels   = None
  cmdChannel = None
  loop       = None

  ##################### constructor ##################### 

  def __init__(self, commandsYamlFn, pw):
    self.ingestCommandYamlFn(commandsYamlFn)
    #self.listCommands()
    self.activateKeyListener()
    self.pw = pw
    self.channels = []

  ##################### key callbacks ##################### 

  def on_press(self, key):
    try:
      #print('alphanumeric key {0} pressed'.format(key.char))
      self.procCh(ch=key.char)
    except AttributeError:
      print('special key {0} pressed'.format(key))

  def on_release(self, key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
      # Stop listener
      return False

  def activateKeyListener(self):
    self.kbListener = keyboard.Listener(on_press=self.on_press,
                                        on_release=self.on_release)
    self.kbListener.start()

  ##################### help ##################### 

  def help(self):
    print("help:: available commands:")
    keys = self.commandHash.keys()
    for key in keys:
      print(key, self.commandHash[key])

  ##################### help ##################### 

  def selfDoc(self, selfCmd):
    print("self documentation called for command " + selfCmd)

  ############## read + process file containing yaml command bindings #############

  def ingestCommandYamlFn(self, sourceYamlFn): 
    try:
      yf = open(sourceYamlFn, 'r+t')
    except:
      print("redYaKb ingestCommandYaml: problem opening file " + sourceYamlFn) 
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
        print("redYaKb ingestCommandYaml: problem parsing command entry: " + commandDescr)

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
        print("redYaKb getCmd: problem with getattr " + commandTxt) 
        e = sys.exc_info()   #e = sys.exc_info()[0]
        print('error: '+str(e))
        return False
    else:
      print("redYaKb getCmd: 'command' not found in commandDescr: " + commandDescr)
      return False

  ##################### list commands ##################### 

  def listCommands(self): 
    if self.commandHash == None:
      print("redYaKb listCommands: commandHash is null (ingestCommandYamlFn likely not called)")
      return False

  ##################### process character #####################

  async def broadcastCmd(self, ch): 
    #print("broadcastCmd ", ch)
    await self.pool.publish(self.cmdChannel, ch)
    #print("broadcastCmd complete")

  ##################### process character #####################

  def procCh(self, ch=None): #if none, will use readCh (blocking)
    print("redYaKb procCh " + ch)
    if ch == None:
      ch = self.readCh()

    if ch in self.commandHash:
      commandDescr = self.commandHash[ch]
      if 'command' in commandDescr:

        commandText = commandDescr['command']
        #print(commandText)
        cmd = self.getCmd(commandDescr)

        if self.cmdChannel == None:
          print("redYaKb procCh error: cmdChannel uninitiated"); return False

        if self.loop == None:
          print("redYaKb procCh error: event loop uninitiated"); return False

        try:
          #print("schedule broadcast")
          self.loop.create_task(self.broadcastCmd(ch))
          cmd()
          return(True)
        except:
          print("redYaKb getCmd: problem with getattr " + commandText) 
          e = sys.exc_info()   #e = sys.exc_info()[0]
          print('error: '+str(e))
          return False

  ##################### redis functions #####################


  async def connect(self): 
    #self.redHand = await aioredis.create_connection(address=(self.host, self.port), 
    #                                                password=self.pw)
    self.pool = await aioredis.create_redis_pool(address=(self.host, self.port), 
                                                    password=self.pw)

  async def testget(self): 
    if self.pool == None:
      print("redWrap error: redis pool not initiated");
      return

    result = await self.pool.execute('hgetall', 'teiDomains');
    print(result)

#################### set up redis publications ####################

  async def pub(self, key, value): 
    if self.pool == None:
      print("redWrap error: redis pool not initiated");
      return

    await self.pool.publish(key, value)

#################### handle message ####################

  async def handle_msg(self, msg):
    print('Received Message:', msg)

#################### reader ####################
  
  async def reader(self, mpsc):  
    async for channel, msg in mpsc.iter():
      assert isinstance(channel, aioredis.AbcChannel)
      print("Received {!r} in channel {!r}".format(msg, channel))

  #https://aioredis.readthedocs.io/en/v1.3.1/mpsc.html
  #https://docs.python.org/3/library/asyncio-task.html
  #https://stackoverflow.com/questions/34118816/aioredis-and-pub-sub-arent-asnyc

#################### set up redis subscriptions ####################

  async def sub(self): 
    if self.pool == None:
      print("redWrap error: redis pool not initiated");
      return

    self.receiver = aioredis.pubsub.Receiver()
    asyncio.create_task(self.reader(self.receiver)) 
    channelArgs = []
    for channelArg in self.channels:
      channelArgs.append(self.receiver.channel(channelArg))
    await self.pool.subscribe(*channelArgs) 

    #https://www.informit.com/articles/article.aspx?p=2979063&seqNum=8
      

### end ###
