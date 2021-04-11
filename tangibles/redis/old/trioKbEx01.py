#https://stackoverflow.com/questions/35223896/listen-to-keypress-with-asyncio

import trio, sys
  
async def main():
  async with trio.lowlevel.FdStream(sys.stdin.fileno()) as stdin:
      async for line in stdin:
        if line.startswith(b'q'):
          break
        print(line)


trio.run(main)

### end ###
