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

  def __init__(self, pw): 
    self.pw = pw

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
  
  async def reader(self, mpsc):  # https://aioredis.readthedocs.io/en/v1.3.1/mpsc.html
    async for channel, msg in mpsc.iter():
      assert is instance(channel, aioredis.AbcChannel)
      print("Got {!r} in channel {!r}".format(msg, channel))


  async def sub(self, key): 
    self.receiver = aioredis.Receiver()
    asyncio.ensure_future(reader(self.receiver))

#################### main ####################

async def main(pw):
  r = redWrap(pw)
  await r.connect()
  await r.testget()

  plinth1 = "hexmap::edu.clemson.edu/computing.tei21/hp01"
  plinth1led = plinth1 + '/led'
  plinth1nfc = plinth1 + '/nfc'
  plinth1cmd = plinth1 + '/cmd'
  update  = "r"
  await r.pub(plinth1cmd, update)

  await r.unsubscript(plinth1)

asyncio.run(main(pw))

### end ###
