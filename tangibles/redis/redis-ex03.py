# Redis hello-world
# Brygg Ullmer, Clemson University
# Begun 2021-03-01

import redis, sys, getch

# take redis password as command-line argument

if len(sys.argv) < 2:
  print("redis hello-world error:")
  print("redis passwd expected as command-line argument")
  sys.exit(-1)


host="redis-15905.c56.east-us.azure.cloud.redislabs.com"
port="15905"
pw  = sys.argv[1]

r=redis.Redis(host=host, port=port, password=pw)

print('Entering blocking keyboard loop')
while True:
  char = getch.getch()
  print(str(int(char))

### later ###

r.hset('teiDomains', 'edu.clemson.computing.tei21', 'https://github.com/ullmer/tei-book/tree/main/tangibles/yaml/edu.clemson/tei21')
r.hset('teiDomains', 'us.sc.k12.pickens.pcva', 'https://github.com/ullmer/tei-book/tree/main/tangibles/yaml/us.sc.k12.pickens/pcva')
print(r.hgetall('teiDomains'))
#{'us.sc.k12.pickens.pcva': '', 'edu.clemson.computing.tei21': ''}

r.hset('hextok::edu.clemson.computing.tei21', 'g01:01', 
  'https://github.com/ullmer/tei-book/tree/main/tangibles/yaml/edu.clemson/tei21/g01/hextok01.yaml')

r.hset('hexplinth::edu.clemson.computing.tei21', 'hp01', 
  'https://github.com.ullmer/tei-book/tree/main/tangibles/yaml/edu.clemson.tei21/hp01.yaml')

r.hset('hexmap::edu.clemson.edu/computing.tei21', 'g01:hm01', 
  'https://github.com/ullmer/tei-book/tree/main/tangibles/yaml/edu.clemson/tei21/g01/hexmap01.yaml')


r.hset('nfc', '59882AA34', 'hextok::edu.clemson.computing.tei21')
r.hset('nfc', '59882AA35', 'hexmap::edu.clemson.edu/computing.tei21')
r.hset('ledmap', 'hexmap::edu.clemson.edu/computing.tei21', '0000AA 00AA00 AA0000 0000AA 00AA00 AA0000')
r.hset('ledstate', 'hexmap::edu.clemson.edu/computing.tei21', 'listeningPattern')
r.hset('ledFoo', 'hexmap::edu.clemson.edu/computing.tei21', 'ledstate')

#names there need refactoring
#trying to allow selection of led maps either
#led-by-led
#or pattern-by-pattern
#(allowing more complex animations, more computational independence, etc.)

### end ###
