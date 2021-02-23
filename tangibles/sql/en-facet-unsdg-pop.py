# Copy states information from Jason Ong yaml into sqlite
# Brygg Ullmer, Clemson University
# Begun 2021-02-03


import json, yaml, sqlite3, sys

yfields = '[code, description, uri, title]'
fields  = yaml.load(yfields)

fn  = 'en-unsdg-list.json'
f   = open(fn, 'r+t')
yd  = json.load(f)
#print(yd[0].keys())
print(fields)

sys.exit(-1)

dbn      = 'en-facet-unsdg.db3'
dbConn   = sqlite3.connect(dbn)
dbCursor = dbConn.cursor()

countryData = []

for sdg in yd:
  populated = {}
  for field in fields:
    try:
      populated[field] = sdg[field]
    except:
  
  abbrev = state['abbreviation']
  name   = state['name']
  stateData.append((abbrev, name))

dbCursor.executemany(
  "insert into enFacetStates (abbrev, name) values (?,?)", 
   stateData)
dbConn.commit()

### end ###
