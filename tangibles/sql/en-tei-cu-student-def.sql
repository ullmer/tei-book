create table enTeiCuStudent (
  id     integer primary key,
  name   text,
  group  integer,
  ug     text,
  cuname text
);

create table enStudentFacet (
  id       integer primary key,
  symname  text,
  filename text
);

create table enStudentFacetRelation (
   id integer primary key,
   studentId integer,
   facetId   integer,
   facetVal  integer
);

create table enTeiCuStudentRaw (
  id     integer primary key,
  rawfields text,fullname text,status text, pgroup text, edu1 text,edu2 text,edu3 text,edu4 text,city1 text,city2 text,city3 text,city4 text,state1 text,state2 text,state3 text,state4 text,country1 text,country1 text,country3 text,country4 text,audience1 text,audience2 text,audience3 text,audience4 text,unsdg1 text,unsdg2 text,unsdg3 text,unsdg4 text,cspantag1 text,cspantag2 text,cspantag3 text,cspantag4 text
);

