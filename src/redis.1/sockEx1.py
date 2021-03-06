#https://stackoverflow.com/questions/48506460/python-simple-socket-client-server-using-asyncio

import asyncio, socket

async def handle_client(reader, writer):
  request = None
  while request != 'quit':
    request = (await reader.read(255)).decode('utf8')
    #response = str(eval(request)) + '\n'
    response = "<{}>\r\n".format(request)
    writer.write(response.encode('utf8'))
    await writer.drain()
  writer.close()

async def run_server():
  server = await asyncio.start_server(handle_client, 'localhost', 15555)
  async with server:
    await server.serve_forever()

asyncio.run(run_server())

### end ###
