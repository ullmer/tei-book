-- US States sqlite table
-- SQL variation by Brygg Ullmer, re python import of this yaml from Jason Ong:
--   https://github.com/jasonong/List-of-US-States.git
-- Begun 2021-02-09

create table enStudentInterestsRaw (
  id    integer primary key,
  fullname  text,
  lastname  text,
  firstname text,
  uname     text,
  inst      text,
  status    text,
  group     integer,
  edu1      text,
  edu2      text,
  edu3      text,
  edu4      text,
  city1     text,
  city2     text,
  city3     text,
  city4     text,
  state1    text,
  state2    text,
  state3    text,
  state4    text,
  country1  text,
  country2  text,
  country3  text,
  country4  text,
  audience1 text,
  audience2 text,
  audience3 text,
  audience4 text,
  unsdg1    text,
  unsdg2    text,
  unsdg3    text,
  unsdg4    text,
  cspantag1 text,
  cspantag2 text,
  cspantag3 text,
  cspantag4 text
);

-- end --

