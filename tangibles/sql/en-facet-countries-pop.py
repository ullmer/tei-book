# Copy countries information subset from Mohammed Le Doze json into sqlite
# Brygg Ullmer, Clemson University
# Begun 2021-02-03

import json, sqlite3

fn  = 'en-facet-countries.json'
f   = open(fn, 'r+t')
yd  = json.load(f)
#print(yd)

dbn      = 'en-facet-countries.db3'
dbConn   = sqlite3.connect(dbn)
dbCursor = dbConn.cursor()

countryData = []

country2languages        = {}
languageAbbrev2countries = {}
languageAbbrev2full      = {}
languageAbbrev2id        = {}

def procLanguages(country, languages):
  global country2languages, languageAbbrev2countries, languageAbbrev2full
  country2languages[country] = languages
  for language in languages:
    (abbrev, full) = language

    if abbrev not in languageAbbrev2countries:
      languageAbbrev2countries[abbrev] = []
    languageAbbrev2countries[abbrev].append(country)

      [country] = .append(country

    
for country in yd:
  name      = country['name']['common']
  abbrev    = country['cioc']
  region    = country['region']
  subregion = country['subregion']
  languages = country['languages']
  entry = (name, abbrev, region, subregion, languages)
  procLanguages(abbrev, languages)
  print(entry)
  countryData.append(entry)

#dbCursor.executemany(
#  "insert into enFacetStates (abbrev, name) values (?,?)", 
#  countryData)
#dbConn.commit()
#
#### end ###
