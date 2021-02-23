# Test attaching plurality of sqlite databases
# Brygg Ullmer, Clemson University
# Begun 2021-02-23

childDBs = {}

metaY = '
 countries: en-facet-countries.db3
 states:    en-facet-states.db3
 SDGs:      en-facet-unsdg.db3
 students:  tei21-cu-students.db3';

import sqlite3
conn = sqlite3.connect('scratch.db3')
c = conn.cursor()

for childDB in childDBs.keys():
  dbFn      = childDBs[childDB]
  attachStr = 'attach database "{}" as {}'.format(dbFn, childDB)
  print(attachStr)

#c.execute('ATTACH DATABASE "db_1.sqlite" AS db_1')
#c.execute('SELECT * FROM db_1.my_table')
#conn.commit()
#c.fetchall()

### end ###

