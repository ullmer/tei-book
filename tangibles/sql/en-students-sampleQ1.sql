# show all Clemson TEI21 students highlighting an interest in UN SDG #5

sqlite> select stud.name from enTeiStudent as stud, enStudentFacetRelation as studrel where studrel.studentId = stud.id and facetId = 100 and facetVal = 5;
Ullmer, Brygg
Bhosekar, Mitali S.
Isaac, Angel Jane J.
Filipiak, Breanna N.
McLendon, Millon M.
Fuller, Corey
Washington, Aika
DuBay, Dylan J.
Everett, Wesley H.
Johnson, Emily A.
Raju Kondur, Shruti Chandrashekar
Singh, Ankita
Enishetty, Manish
Michael, Ishitha
LU, YUN

# show how many Clemson TEI21 students highlighted an interest in each UN SDG (facetID 100)
sqlite> select studrel.facetVal, count(stud.name) from enTeiStudent as stud, enStudentFacetRelation as studrel where studrel.studentId = stud.id and facetId = 100 group by facetVal;
1|8
2|7
3|8
4|12
5|15
6|2
7|6
8|5
9|7
10|7
11|2
12|4
13|8
14|2
15|2
16|1
17|3
18|1
