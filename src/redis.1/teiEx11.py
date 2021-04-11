# Use keyboard to express events via redis for relaying to RPi++ based upon YAML cfg
# Brygg Ullmer, Clemson University
# Begun 2021-03-01

import sys
import asyncio
import aioredis # async I/O redis libraries

from    rykEx11 import *
cyfn = 'rykEx11.yaml' #commands yaml filename

# take redis password as command-line argument

if len(sys.argv) < 2:
  print("redis hello-world error:")
  print("redis passwd expected as command-line argument")
  sys.exit(-1)

pw = sys.argv[1]

#################### main ####################

async def periodic():
  while True:
    print(".", end='', flush=True)
    await asyncio.sleep(.5)
    #for reasons I don't understand, probably involving curious interactions between
    # pynput threading and asyncio, absent this function, the event loop
    # isn't serviced for pubsub broadcasts. long sigh.

async def main(pw):
  global loop
  print("we're running")

  ryk  = rykEx11(cyfn, pw)
  await ryk.connect()
  await ryk.testget()

  p1    = "edu.clemson.edu/computing.tei21/hp01" #hex plinth #1
  p1pat = p1 + "/*"  # allows subscription to multiple associated channels
  p1led = p1 + '/led'
  p1nfc = p1 + '/nfc'
  p1cmd = p1 + '/cmd'

  ryk.channels   = [p1led, p1nfc, p1cmd]
  ryk.cmdChannel = p1cmd #redYaKb will broadcast commands to this address
  ryk.loop       = loop  #hacky; used to pass event loop for scheduling async actions

  await ryk.psub(p1pat) # should show how this is used

global loop
loop = asyncio.get_event_loop()
loop.create_task(periodic())
loop.create_task(main(pw))
loop.run_forever()
loop.close()

### end ###
