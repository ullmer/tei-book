# Integration fo enHexPlinthSim with asyncio and aioredis
# Brygg Ullmer and TBD, Clemson University
# Begun 2021-04-11

#https://www.reddit.com/r/Python/comments/33ecpl/neat_discovery_how_to_combine_asyncio_and_tkinter/

#https://gist.github.com/nameoftherose/037e97b95d94df7867ee328ea8009857

#https://stackoverflow.com/questions/47895765/use-asyncio-and-tkinter-or-another-gui-lib-together-without-freezing-the-gui

from tkinter import *
import asyncio

from enHexPlinthSim1c import *

async def periodic():
  while True:
    print(".", end='', flush=True)
    await asyncio.sleep(.5)
    #for reasons I don't understand, probably involving curious interactions between
    # pynput threading and asyncio, absent this function, the event loop
    # isn't serviced for pubsub broadcasts. long sigh.

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

async def main(async_loop):
  colorTeiCrim = '#851c16'

  ehps = enHexPlinthSim()
  ehps.buildGui()
  #ehps.changeLEDSimColor(5, colorTeiCrim)
  ehps.changeLEDSimColor(4, colorTeiCrim)
  #ehps.root.mainloop()
  await run_tk(ehps.root)

if __name__ == '__main__':
    aloop = asyncio.get_event_loop()
    aloop.create_task(periodic())
    aloop.create_task(main(aloop))
    aloop.run_forever()
    aloop.close()

    #main(async_loop)

### end ###
