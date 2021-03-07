# Redis hello-world
# Brygg Ullmer, Clemson University
# Begun 2021-03-01

import sys
from rykTeiEx04 import *
cyfn = 'rykTeiEx04.yaml' #commands yaml filename
ryk = rykTeiEx04(cyfn)

print('Entering blocking keyboard loop.  Press "h" for help=list of commands.')

while True:
  ryk.procCh()

### end ###
