# Brygg Ullmer, Clemson University
# Begun 2021-03-04

import json
import redis, sys

fn  = 'colors1.json'
f   = open(fn, 'r+t')
jd  = json.load(f)
print(jd[0])

# take redis password as command-line argument
if len(sys.argv) < 2:
  print("redis hello-world error:")
  print("redis passwd expected as command-line argument")
  sys.exit(-1)

host="redis-15905.c56.east-us.azure.cloud.redislabs.com"
port="15905"
pw  = sys.argv[1]

r=redis.Redis(host=host, port=port, password=pw)

for color in jd:
  name = color['name']
  hex = color['hex']

  r.hset('colormap01', name, hex)

### end ###
