# Copy states information from Jason Ong yaml into sqlite
# Brygg Ullmer, Clemson University
# Begun 2021-02-03

import yaml, sqlite3

fn  = 'en-facet-states.yml'
f   = open(fn, 'r+t')
yd  = yaml.load(f)
#print(yd)

dbn      = 'en-facet-states.db3'
dbConn   = sqlite3.connect(dbn)
dbCursor = dbConn.cursor()

stateData = []

for state in yd:
  abbrev = state['abbreviation']
  name   = state['name']
  stateData.append((abbrev, name))

dbCursor.executemany(
  "insert into enFacetStates (abbrev, name) values (?,?)", 
   stateData)
dbConn.commit()

### end ###
