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

pw      = sys.argv[1]

class redWrap:    #asyncio ~wrapper of redis functionality
  host    = "redis-15905.c56.east-us.azure.cloud.redislabs.com"
  port    = "15905"
  pw      = None
  redHand = None  #redis handle

  def __init__(self, pw): 
    self.pw = pw

  async def connect(self): 
    self.redHand = await aioredis.Redis(host=self.host, 
                                        port=self.port, password=self.pw)

async def main(pw):
  r = redWrap(pw)
  r = await r.connect()

asyncio.run(main(pw))

### end ###
