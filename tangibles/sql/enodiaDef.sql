# Initial population for Enodia tables
# en prefix short for Enodia; enHt, for Enodia hextok
# Initial definition by Brygg Ullmer
# Begun 2021-02-02

create table enFacets {
  id    int primary key,
  name  text,
  descr text,
};

create table enHtClass {
 id   int primary key,
 name text,
 descr text
};

create table enHtFacetClass {
 id    int primary key,
 class int, % references enHtClass.id
 name  text,
 descr text
};

create table enHtFacetInst {
  id    int primary key,
  facet int % references enHtFacetClass.id,
  value text
};

%%% end %%%

