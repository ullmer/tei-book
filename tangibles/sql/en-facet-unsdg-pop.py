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

#sys.exit(-1)

dbn      = 'en-facet-unsdg.db3'
dbConn   = sqlite3.connect(dbn)
dbCursor = dbConn.cursor()

rows = []
for sdg in yd:
  populated = {}; row = []
  for field in fields:
    try:
      populated[field] = sdg[field]
      row.append(sdg[field])
    except:
      print('yaml/json error processing ' + field)
      e = sys.exc_info()   #e = sys.exc_info()[0]
      print('error: '+str(e))
  rows.append(row)

compactFields = ','.join(fields)
insert = "insert into enFacetUNSDG ({}) values (?,?,?,?)".format(compactFields)
print("insertion: "+ insert)

dbCursor.executemany(insert, rows)
dbConn.commit()

### end ###
