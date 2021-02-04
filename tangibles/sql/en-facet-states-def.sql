-- US States sqlite table
-- SQL variation by Brygg Ullmer, re python import of this yaml from Jason Ong:
--   https://github.com/jasonong/List-of-US-States.git
-- Begun 2021-02-03

create table enFacetStates (
  id    integer primary key,
  abbrev text,
  name  text
);

-- end --

