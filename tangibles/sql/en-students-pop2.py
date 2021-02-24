# Brygg Ullmer, Clemson University
# Begun 2021-02-03

import enTableSql, sys, sqlite3

fn  = 'tei21-cu-students.csv'
dfn  = 'tei21-cu-students.db3'
enTable = enTableSql.enTableSql(fn)
#enTable.insertSqlRaw(dfn)

#print(enTable.rows2)

studIdxs = [2, 5, 3]; studrows = []; studentId = 1
sdgIdxs  = [27, 28, 29, 30]; sdgrows = []
    
#insert into enStudentFacet (id, symname) values (100, 'unsdg');

for row in enTable.rows2:
  studrow = [studentId]
  for idx in studIdxs:
    studrow.append(row[idx])
  studrows.append(studrow)

  for idx in sdgIdxs:
    sdg = row[idx]
    sdgrows.append([100, studentId, int(sdg)])
  studentId+=1

#print(studrows)
#print(sdgrows)

conn = sqlite3.connect(dfn)
c = conn.cursor()

c.executemany(
   "insert into enTeiStudent (id, name, sgroup, ug) values (?,?,?,?)", 
    studrows)
conn.commit()

c.executemany(
  "insert into enStudentFacetRelation (facetId, studentId, facetVal) values (?,?,?)", 
   sdgrows)
conn.commit()

#### end ###
