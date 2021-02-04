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

