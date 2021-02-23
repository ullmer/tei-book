-- UN SDG sqlite table
-- SQL variation by Brygg Ullmer, re python import of this json from UN:
--    https://unstats.un.org/SDGAPI/v1/sdg/Goal/List?includechildren=true
--    https://unstats.un.org/sdgapi/swagger/
-- Begun 2021-02-23

create table enFacetUNSDG (
  id          integer primary key,
  code        integer, 
  title       text,
  description text, 
  uri         text 
);


-- end --

