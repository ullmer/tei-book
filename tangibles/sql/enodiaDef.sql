-- Initial population for Enodia tables
-- en prefix short for Enodia; enHt, for Enodia hextok
-- Initial definition by Brygg Ullmer
-- Begun 2021-02-02

create table enFacets (
  id    integer primary key,
  name  text,
  descr text
);

create table enHtClass (
 id    integer primary key,
 name  text,
 descr text
);

create table enHtPerson (
  id       integer primary key,
  handle   text,
  name     text,
  uname    text,
  groupId  text 
);

create table enHtFacet (
  id       integer primary key,
  facetId  integer,
  facetVal text
);

-- end --

