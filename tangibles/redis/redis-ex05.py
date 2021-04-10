# Redis hello-world
# Brygg Ullmer, Clemson University
# Begun 2021-03-01

import sys
import aioredis # async I/O redis librarires
from rykTei21Base import *

cyfn = 'tei21-commands.yaml' #commands yaml filename

ryk = rykTei21Base(cyfn)

print('Entering blocking keyboard loop')

while True:
  ryk.procCh()

sys.exit(-1)

# take redis password as command-line argument

if len(sys.argv) < 2:
  print("redis hello-world error:")
  print("redis passwd expected as command-line argument")
  sys.exit(-1)

host="redis-15905.c56.east-us.azure.cloud.redislabs.com"
port="15905"
pw  = sys.argv[1]

#r=redis.Redis(host=host, port=port, password=pw)

async def connect(): 
  global r
  r=await aioredis.Redis(host=host, port=port, password=pw)

connect()

### end ###
