# Brygg Ullmer, Clemson University
# Begun 2021-02-03

import csv, sqlite3, sys

df = {} #data fields
df[2]  = 'fullname'
df[3]  = 'status'
df[4]  = 'group'
df[7]  = 'edu1';   df[8]  = 'edu2';   df[9]  = 'edu3';   df[10] = 'edu4'
df[11] = 'city1';  df[12] = 'city2';  df[13] = 'city3;   df[14] = 'city4'
df[15] = 'state1'; df[16] = 'state2'; df[17] = 'state3'; df[18] = 'state4'
df[19]='country1'; df[20]='country2'; df[21]='country3'; df[22]='country4'
df[23]='audience1';df[24]='audience2';df[25]='audience3';df[26]='audience4'
df[27]= 'unsdg1';  df[28]=   'unsdg2';df[29]=   'unsdg3';df[30]=   'unsdg4'
df[31]='cspantag1';df[32]='cspantag2';df[33]='cspantag3';df[34]='cspantag4'
 
fn  = 'tei21-cu-students.csv'
f   = open(fn, 'r+t')
cr  = csv.reader(f)

for row in cr:
   print(row[7])

sys.exit(1)

dbn      = 'en-facet-countries.db3'
dbConn   = sqlite3.connect(dbn)
dbCursor = dbConn.cursor()

countryData = []

countryAbbrev2Full       = {}
country2languages        = {}
languageAbbrev2countries = {}
languageAbbrev2full      = {}
languageAbbrev2id        = {}
country2region           = {}
country2subregion        = {}
region2countries         = {}
subregion2countries      = {}
subregion2region         = {}

#################### process languages ####################

def procLanguages(country, languages):
  global country2languages, languageAbbrev2countries, languageAbbrev2full
  country2languages[country] = languages
  abbrevs = languages.keys()
  for abbrev in abbrevs:
    full = languages[abbrev]

    if abbrev not in languageAbbrev2countries:
      languageAbbrev2countries[abbrev] = []

    languageAbbrev2countries[abbrev].append(country)
    languageAbbrev2full[abbrev] = full

#################### process  region ####################

def procRegion(country, region, subregion):
  global country2region, country2subregion, region2countries, subregion2countries, subregion2region

  locale = (region, subregion)
  country2region[country]    = locale
  country2subregion[country] = subregion
  if region not in region2countries:
    region2countries[region] = []

  region2countries[region].append(country)

  if subregion not in subregion2countries:
    subregion2countries[subregion] = []
  subregion2countries[subregion].append(country)
  subregion2region[subregion] = region
  
#################### main ####################

for country in yd:
  name      = country['name']['common']
  abbrev    = country['cioc']
  region    = country['region']
  subregion = country['subregion']
  languages = country['languages']

  countryAbbrev2Full[abbrev] = name

  entry = (name, abbrev, region, subregion, languages)

  procLanguages(abbrev, languages)
  procRegion(abbrev, region, subregion)

  #print(entry)
  #countryData.append(entry)

############ populate region/subregion table ############

subregion2id = {}; id=1
#if False:
if True:
  #print(str(subregion2region))
  print("REGION INSERTIONS")
  regionData = []
  for subregion in subregion2region.keys():
    region = subregion2region[subregion]
    regionData.append((id,region, subregion))
    id+=1
    subregion2id[subregion]=id
  print(str(regionData))

  dbCursor.executemany(
    "insert into enFacetWorldRegions (id, region, subregion) values (?,?,?)", 
    regionData)
  dbConn.commit()

############ populate countries table ############

country2id = {}; countryId=1
if True:
  countries = country2region.keys()
  for countryAbbrev in countries:
    subregion   = country2subregion[countryAbbrev]
    subregionId = subregion2id[subregion]
    countryFull = countryAbbrev2Full[countryAbbrev]
    countryData.append((countryId, countryAbbrev, countryFull, subregionId))
    countryId += 1

  dbCursor.executemany(
    "insert into enFacetCountries (id, abbrev, name, subregionId) values (?,?,?,?)", 
    countryData)
  dbConn.commit()

############ populate languages table ############

if False:
#if True:
  print(str(subregion2region))
  print("REGION INSERTIONS")
  regionData = []
  for subregion in subregion2region.keys():
    region = subregion2region[subregion]
    regionData.append((id, region, subregion))
  print(str(regionData))

  dbCursor.executemany(
    "insert into enFacetWorldRegions (id, region, subregion) values (?,?,?)", 
    regionData)
  dbConn.commit()


#### end ###