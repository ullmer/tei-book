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
  pool = None  #redis handle

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

#################### main ####################

async def main(pw):
  r = redWrap(pw)
  await r.connect()
  await r.testget()

  plinth1 = "hexmap::edu.clemson.edu/computing.tei21/hp01"
  update  = "r"
  await r.pub(plinth1, update)

asyncio.run(main(pw))

### end ###
