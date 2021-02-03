-- populate sample database
-- By Brygg Ullmer
-- Begun 2021-02-02

insert into enFacets (name)
  values ('edu'), ('cities'), ('states'),
    ('audiences'), ('unsdg'), ('cspantags');

insert into enHtPerson (handle, name, uname, groupId) 
  values ('person.edu.clemson.bullmer', 'Brygg Ullmer', 
          'bullmer', '1');

insert into enHtFacet (facetId, facetVal) values
  (3, 'SC'), (3, 'LA'), (3, 'MA'), (3, 'KY');

insert into enHtFacet (facetId, facetVal) values
  (fi, 'Lexington'), (fi, 'Berlin'), 
  (fi, 'Boston'), (fi, 'Palo Alto')
 where select enFacets.id as fi
   from enFacets where enFacets.name = 'cities';


insert into enHtFacetInst (facetId, value)
  values (facetId, 'SC')
  select facetId from enHtFacetClass where
    enHtFacetClass.name = 'states';

create table enHtFacetClass (
 id      integer primary key,
 classId integer, -- references enHtClass.id
 name    text,
 descr   text
);

create table enHtFacetInst (
  id      integer primary key,
  facetId integer -- references enHtFacetClass.id,


select * from enFacets, enHtFacetClass
  where enFacets.name='states';

select @facetId=[id] from enFacets where name='states';
print  @facetId;

insert into enHtFacetInst (city)
  

if not exists (select id from enFacetClass
               where enFacetClass.name = 'edu'

'GSSM')


insert into enHtFacetInst (
  enFacet
 where enFF



create table enFacet (
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
  facetId  integer -- references enHtFacetClass.id,
  facetVal text
);

-- end --

