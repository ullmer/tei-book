-- Countries sqlite table
-- SQL variation by Brygg Ullmer, re python import of this yaml from Jason Ong:
--    https://github.com/mledoze/countries
-- Begun 2021-02-03

create table enFacetCountries (
  id          integer primary key,
  abbrev      text,
  name        text,
  subregionId integer
);

create table enFacetWorldRegions (
  id        integer primary key,
  region    text,
  subregion text
);

create table enFacetWorldLanguages (
  id     integer primary key,
  name   text,
  abbrev text
);

create table enFacetCountryLanguage (
  id         integer primary key,
  countryId  integer,
  languageId integer
);

-- end --

