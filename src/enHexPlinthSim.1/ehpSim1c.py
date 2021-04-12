# Integration fo enHexPlinthSim with asyncio and aioredis
# Brygg Ullmer and TBD, Clemson University
# Begun 2021-04-11

#the below draws from these sources
#https://www.reddit.com/r/Python/comments/33ecpl/neat_discovery_how_to_combine_asyncio_and_tkinter/
#https://gist.github.com/nameoftherose/037e97b95d94df7867ee328ea8009857
#https://stackoverflow.com/questions/47895765/use-asyncio-and-tkinter-or-another-gui-lib-together-without-freezing-the-gui

from tkinter import *
import asyncio

from enHexPlinthSim1c import *

async def heartbeat():
  while True:
    print(".", end='', flush=True)
    await asyncio.sleep(1)

async def toggleLEDs():
  global ehps, colorTeiCrim
  while True:
    for i in range(6):
      if i>0: j=i-1
      else:   j=5
      if ehps != None:
        ehps.changeLEDSimColor(i, colorTeiCrim)
        ehps.muteLEDSimColor(j)
      await asyncio.sleep(1)

async def run_tk(root, interval=0.1):  #original interval = 0.05
  try:
    while True:
      root.update()
      #yield from asyncio.sleep(interval)
      await asyncio.sleep(interval)
  except tkinter.TclError as e:
    if "application has been destroyed" not in e.args[0]:
      raise

#################### main ####################
global ehps, colorTeiCrim
ehps = None
colorTeiCrim = '#851c16'

async def main(async_loop):
  global ehps, colorTeiCrim
  ehps = enHexPlinthSim()
  ehps.buildGui()
  await run_tk(ehps.root)

if __name__ == '__main__':
    aloop = asyncio.get_event_loop()
    aloop.create_task(heartbeat())
    aloop.create_task(toggleLEDs())
    aloop.create_task(main(aloop))
    aloop.run_forever()
    aloop.close()

    #main(async_loop)

### end ###
