#https://stackoverflow.com/questions/48506460/python-simple-socket-client-server-using-asyncio


###### Redis pubsub/socket gateway
# Brygg Ullmer (Clemson U.) 
# Begun 2021-04-14

# https://pypi.org/project/pynput/
# https://stackoverflow.com/questions/53088995/pynput-keyboard-listener-does-not-detect-keys-on-mac-os-x
# on Mac, one must go to System Preferences -> Security and Privacy -> Privacy -> 
# Accessibility, and add "Terminal" to "Allow the apps below to control your 
# computer" (if you are running Python or Python3 from Terminal)

import sys
import yaml
import redis 
import socket
import asyncio
import aioredis 

# python3 -m pip install redis pyyaml aioredis

##################### redis yaml keyboard class #####################

class redSock:

  commandHash      = None

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

  ##################### help ##################### 

  def help(self):
    print("help:: available commands:")
    keys = self.commandHash.keys()
    for key in keys:
      print(key, self.commandHash[key])

  ##################### process character #####################

  async def broadcastCmd(self, ch): 
    #print("broadcastCmd ", ch)
    await self.pool.publish(self.cmdChannel, ch)
    #print("broadcastCmd complete")

  ##################### process character #####################

  def procCh(self, ch=None): #if none, will use readCh (blocking)
    #print("redYaKb procCh " + ch)
    print("[" + ch + "]", end='', flush=True)
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
    self.pool = await aioredis.create_redis_pool(address=(self.host, self.port), 
                                                    password=self.pw)

  async def testget(self): 
    if self.pool == None:
      print("redYaKb error: redis pool not initiated");
      return

    result = await self.pool.execute('hgetall', 'teiDomains');
    print(result)

#################### set up redis publications ####################

  async def pub(self, key, value): 
    if self.pool == None:
      print("redYaKb error: redis pool not initiated");
      return

    await self.pool.publish(key, value)

#################### handle message ####################

  async def handle_msg(self, msg):
    print("<<{}>>".format(msg))

#################### reader ####################
  
  async def reader(self, mpsc):  
    async for channel, msg in mpsc.iter():
      assert isinstance(channel, aioredis.abc.AbcChannel)
      #print("Received {!r} in channel {!r}".format(msg, channel))
      print("[{!r}]")
      key, value = msg
      valDecode = value.decode("utf-8") 
      await self.handle_msg(valDecode)

  #https://aioredis.readthedocs.io/en/v1.3.1/mpsc.html
  #https://docs.python.org/3/library/asyncio-task.html
  #https://stackoverflow.com/questions/34118816/aioredis-and-pub-sub-arent-asnyc

#################### set up redis subscriptions ####################

  async def sub(self): 
    if self.pool == None:
      print("redYaKb sub error: redis pool not initiated");
      return

    self.receiver = aioredis.pubsub.Receiver()
    asyncio.create_task(self.reader(self.receiver)) 
    channelArgs = []
    for channelArg in self.channels:
      channelArgs.append(self.receiver.channel(channelArg))
    await self.pool.subscribe(*channelArgs) 

    #https://www.informit.com/articles/article.aspx?p=2979063&seqNum=8
      
#################### set up redis subscriptions ####################

  async def psub(self, targPattern): 
    if self.pool == None:
      print("redYaKb psub error: redis pool not initiated");
      return

    #https://aioredis.readthedocs.io/en/v1.3.1/mpsc.html
    self.receiver = aioredis.pubsub.Receiver()
    asyncio.create_task(self.reader(self.receiver)) 
    psubHandle    = self.receiver.pattern(targPattern)
    await self.pool.psubscribe(psubHandle) 

  async def handle_client(reader, writer):
    request = None
    while request != 'quit':
      request = (await reader.read(255)).decode('utf8')
      #response = str(eval(request)) + '\n'
      response = "<{}>\r\n".format(request)
      writer.write(response.encode('utf8'))
      await writer.drain()
    writer.close()
  
  async def run_server():
    server = await asyncio.start_server(handle_client, 'localhost', 15555)
    async with server:
      await server.serve_forever()
  
  asyncio.run(run_server())
  
### end ###
