# Redis hello-world
# Brygg Ullmer, Clemson University
# Begun 2021-03-01

import sys
import asyncio
import getch
#import aioredis # async I/O redis libraries
#import concurrent.futures

#https://docs.python.org/3/library/asyncio-eventloop.html

def blocking_io():
  ch = getch()
  print("<" + ch + ">")

async def main():
  loop = asyncio.get_running_loop()

  result = await loop.run_in_executor(None, blocking_io)
  print('default thread pool', result)

asyncio.run(main())

### end ###
