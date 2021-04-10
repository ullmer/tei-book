# Redis hello-world
# Brygg Ullmer, Clemson University
# Begun 2021-03-01

import sys
import asyncio
import getch
#import concurrent.futures

#https://docs.python.org/3/library/asyncio-eventloop.html

def blocking_io():
  ch = getch.getch()
  print("<" + ch + ">")

async def main():
  loop = asyncio.get_running_loop()
  while True:
    await loop.run_in_executor(None, blocking_io)

#asyncio.run(main())

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
loop.close()

### end ###
