# Redis hello-world
# Brygg Ullmer, Clemson University
# Begun 2021-03-01

import sys
import asyncio
import aioredis # async I/O redis libraries

from    rykTeiEx04 import *
cyfn = 'rykTeiEx04.yaml' #commands yaml filename

# take redis password as command-line argument

if len(sys.argv) < 2:
  print("redis hello-world error:")
  print("redis passwd expected as command-line argument")
  sys.exit(-1)

pw = sys.argv[1]

#################### main ####################

async def main(pw):
  print("main runs")

  ryk  = rykTeiEx04(cyfn, pw)
  await ryk.connect()
  await ryk.testget()

  p1    = "hexmap::edu.clemson.edu/computing.tei21/hp01"
  p1pat =  p1 + "/*"
  p1led = p1 + '/led'
  p1nfc = p1 + '/nfc'
  p1cmd = p1 + '/cmd'

  ryk.channels   = [p1led, p1nfc, p1cmd]
  ryk.cmdChannel = p1cmd

  #pat = ryk.receiver.pattern(p1pat)
  await ryk.pool.psubscribe(p1pat)

  #await ryk.pub(p1cmd, update)

  #await r.unsubscribe(p1)

#asyncio.run(main(pw))

loop = asyncio.get_event_loop()
loop.create_task(main(pw))
loop.run_forever()
loop.close()

### end ###
