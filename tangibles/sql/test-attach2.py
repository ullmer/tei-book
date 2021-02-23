# Test attaching plurality of sqlite databases
# Brygg Ullmer, Clemson University
# Begun 2021-02-23

import yaml, sys

scratchDBN = 'scratch.db3'
childDBY = """
 countries: common/en-facet-countries.db3 
 states:    common/en-facet-states.db3 
 SDGs:      common/en-facet-unsdg.db3 
 students:  edu.clemson/tei21-cu-students.db3""";

childDBs = yaml.load(childDBY) #both supports compactness
print(childDBs)

import sqlite3
conn = sqlite3.connect(scratchDBN)
c = conn.cursor()

for childDB in childDBs.keys():
  dbFn      = childDBs[childDB]
  attachStr = 'attach database "{}" as {};'.format(dbFn, childDB)
  print(attachStr)
  c.execute(attachStr);
  #c.execute('SELECT * FROM {}.my_table'.format(childDB)
#conn.commit()
#c.fetchall()

### end ###

