# Redis hello-world
# Brygg Ullmer, Clemson University
# Begun 2021-03-01

import sys
import asyncio
import aioredis # async I/O redis libraries

# take redis password as command-line argument

if len(sys.argv) < 2:
  print("redis hello-world error:")
  print("redis passwd expected as command-line argument")
  sys.exit(-1)

pw = sys.argv[1]

#################### asyncio ~wrapper of redis functionality ####################

class redWrap:    
  host = "redis-15905.c56.east-us.azure.cloud.redislabs.com"
  port = "15905"
  pw   = None
  pool     = None  #redis handle
  receiver = None
  channels = None

  def __init__(self, pw): 
    self.pw = pw
    self.channels = []

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

  async def pub(self, key, value): 
    if self.pool == None:
      print("redWrap error: redis pool not initiated");
      return

    await self.pool.publish(key, value)

  async def handle_msg(self, msg):
    print('Received Message:', msg)
  
  async def reader(self, mpsc):  # https://aioredis.readthedocs.io/en/v1.3.1/mpsc.html
    async for channel, msg in mpsc.iter():
      assert isinstance(channel, aioredis.AbcChannel)
      print("Received {!r} in channel {!r}".format(msg, channel))

  #https://docs.python.org/3/library/asyncio-task.html
  #https://stackoverflow.com/questions/34118816/aioredis-and-pub-sub-arent-asnyc

  async def sub(self): 
    #self.receiver = aioredis.pubsub.Receiver(loop=loop)
    self.receiver = aioredis.pubsub.Receiver()
    asyncio.create_task(self.reader(self.receiver)) 
    channelArgs = []
    for channelArg in self.channels:
      channelArgs.append(self.receiver.channel(channelArg))
    await aioredis.abc.redis.subscribe(*channelArgs) 

    #https://www.informit.com/articles/article.aspx?p=2979063&seqNum=8
      
#################### main ####################

async def main(pw):
  r = redWrap(pw)
  await r.connect()
  await r.testget()

  p1    = "hexmap::edu.clemson.edu/computing.tei21/hp01"
  p1led = p1 + '/led'
  p1nfc = p1 + '/nfc'
  p1cmd = p1 + '/cmd'
  r.channels = [p1led, p1nfc, p1cmd]
  #await r.pub(p1cmd, update)
  await r.sub()

  update  = "r"
  #await r.unsubscribe(p1)

asyncio.run(main(pw))

#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())
#loop.close()

### end ###
