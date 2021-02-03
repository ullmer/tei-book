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

create table enHtFacetClass (
 id    integer primary key,
 class integer, -- references enHtClass.id
 name  text,
 descr text
);

create table enHtFacetInst (
  id    integer primary key,
  facet integer -- references enHtFacetClass.id,
  value text
);

-- end --

