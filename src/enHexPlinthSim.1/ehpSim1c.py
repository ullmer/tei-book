#https://stackoverflow.com/questions/47895765/use-asyncio-and-tkinter-or-another-gui-lib-together-without-freezing-the-gui

from tkinter import *
import asyncio
import threading
import random

from enHexPlinthSim1c import *

def _asyncio_thread(async_loop):
    async_loop.run_until_complete(do_urls())

def do_tasks(async_loop):
    """ Button-Event-Handler starting the asyncio part. """
    threading.Thread(target=_asyncio_thread, args=(async_loop,)).start()

async def one_url(url):
    """ One task. """
    sec = random.randint(1, 8)
    await asyncio.sleep(sec)
    return 'url: {}\tsec: {}'.format(url, sec)

async def do_urls():
    """ Creating and starting 10 tasks. """
    tasks = [one_url(url) for url in range(10)]
    completed, pending = await asyncio.wait(tasks)
    results = [task.result() for task in completed]
    print('\n'.join(results))

#################### main ####################

def main(async_loop):
  colorTeiCrim = '#851c16'

  ehps = enHexPlinthSim()
  ehps.buildGui()
  #ehps.changeLEDSimColor(5, colorTeiCrim)
  ehps.changeLEDSimColor(4, colorTeiCrim)
  ehps.root.mainloop()

if __name__ == '__main__':
    async_loop = asyncio.get_event_loop()
    main(async_loop)

### end ###
