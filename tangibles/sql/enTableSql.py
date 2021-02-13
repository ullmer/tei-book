# SQL & SqLite support for tables
# Brygg Ullmer, Clemson University
# Begun 2021-02-03

import csv, sqlite3, sys

class enTableSql:
  rawfieldsName = 'rawfields'
  rawgroupsName = 'rawgroups'

  fn     = None #file name
  fh     = None #file handle
  reader = None #csv reader
  df     = {}   #data fields
  rows   = None #data rows (raw table itself)

############### readCsvTable ############### 

  def readCsvTable(self, fn):
    self.fn = fn
    self.fh = open(fn, 'r+t')
    self.reader = csv.reader(self.fh)

    self.rows = []
    for row in self.reader:
      self.rows.append(row)

############### print table dimensions ############### 

  def printTableDimensions(self):
    numRows = len(self.rows); numCols = len(self.rows[0])
    print("table dimensions: %s x %s" % (numRows, numCols))
  
############### check raw header ############### 

  def checkRawHeader(self):
    if self.rows == None:
      print("Error: enTableSql.checkRawHeader expects populated rows")
      return False

    rfName = self.rows[0][0]; rgName = self.rows[1][0]

    if ((rfName != self.rawfieldsName) or
        (rgName != self.rawgroupsName)):
      print("Error: enTableSql.checkRawHeader expects cells A1 and B1 to hold")
      print("values %s and %s; and right-adjacent cells" % (rfName, rgName))
      print("to be populated appropriately")
      print(":: actual vals: %s, %s" % (rfName, rgName))
      return False
    return True
    
############### process header ############### 

  def procHeader(self):
    headerOk = self.checkRawHeader()
    if headerOk == False:
      return False

    idxList1 = {}; idxList2 = {}
    row1 = self.rows[0]; row2 = self.rows[1]
    idx = 0 
    for col in row1: #build map of columns in row 1
      if col not in idxList1: 
        idxList1[col] = []
      idxList1[col].append(idx); idx += 1

    idx = 0
    for col in row2: #repeat for row 2
      if col not in idxList2: 
        idxList2[col] = []
      idxList2[col].append(idx); idx += 1

    print("row1:" + str(idxList1))
    print("row2:" + str(idxList2))

    return True
      
############### constructor ############### 

  def __init__(self, filename):
    self.readCsvTable(filename)
    self.printTableDimensions()
    headerOk = self.procHeader()
    if headerOk == False:
      return None



#enTableSql.processTable(rows)

#sys.exit(1)
#
#dbn      = 'en-facet-countries.db3'
#dbConn   = sqlite3.connect(dbn)
#dbCursor = dbConn.cursor()
#
#countryData = []
#
#countryAbbrev2Full       = {}
#country2languages        = {}
#languageAbbrev2countries = {}
#languageAbbrev2full      = {}
#languageAbbrev2id        = {}
#country2region           = {}
#country2subregion        = {}
#region2countries         = {}
#subregion2countries      = {}
#subregion2region         = {}
#
##################### process languages ####################
#
#def procLanguages(country, languages):
#  global country2languages, languageAbbrev2countries, languageAbbrev2full
#  country2languages[country] = languages
#  abbrevs = languages.keys()
#  for abbrev in abbrevs:
#    full = languages[abbrev]
#
#    if abbrev not in languageAbbrev2countries:
#      languageAbbrev2countries[abbrev] = []
#
#    languageAbbrev2countries[abbrev].append(country)
#    languageAbbrev2full[abbrev] = full
#
##################### process  region ####################
#
#def procRegion(country, region, subregion):
#  global country2region, country2subregion, region2countries, subregion2countries, subregion2region
#
#  locale = (region, subregion)
#  country2region[country]    = locale
#  country2subregion[country] = subregion
#  if region not in region2countries:
#    region2countries[region] = []
#
#  region2countries[region].append(country)
#
#  if subregion not in subregion2countries:
#    subregion2countries[subregion] = []
#  subregion2countries[subregion].append(country)
#  subregion2region[subregion] = region
#  
##################### main ####################
#
#for country in yd:
#  name      = country['name']['common']
#  abbrev    = country['cioc']
#  region    = country['region']
#  subregion = country['subregion']
#  languages = country['languages']
#
#  countryAbbrev2Full[abbrev] = name
#
#  entry = (name, abbrev, region, subregion, languages)
#
#  procLanguages(abbrev, languages)
#  procRegion(abbrev, region, subregion)
#
#  #print(entry)
#  #countryData.append(entry)
#
############# populate region/subregion table ############
#
#subregion2id = {}; id=1
##if False:
#if True:
#  #print(str(subregion2region))
#  print("REGION INSERTIONS")
#  regionData = []
#  for subregion in subregion2region.keys():
#    region = subregion2region[subregion]
#    regionData.append((id,region, subregion))
#    id+=1
#    subregion2id[subregion]=id
#  print(str(regionData))
#
#  dbCursor.executemany(
#    "insert into enFacetWorldRegions (id, region, subregion) values (?,?,?)", 
#    regionData)
#  dbConn.commit()
#
############# populate countries table ############
#
#country2id = {}; countryId=1
#if True:
#  countries = country2region.keys()
#  for countryAbbrev in countries:
#    subregion   = country2subregion[countryAbbrev]
#    subregionId = subregion2id[subregion]
#    countryFull = countryAbbrev2Full[countryAbbrev]
#    countryData.append((countryId, countryAbbrev, countryFull, subregionId))
#    countryId += 1
#
#  dbCursor.executemany(
#    "insert into enFacetCountries (id, abbrev, name, subregionId) values (?,?,?,?)", 
#    countryData)
#  dbConn.commit()
#
############# populate languages table ############
#
#if False:
##if True:
#  print(str(subregion2region))
#  print("REGION INSERTIONS")
#  regionData = []
#  for subregion in subregion2region.keys():
#    region = subregion2region[subregion]
#    regionData.append((id, region, subregion))
#  print(str(regionData))
#
#  dbCursor.executemany(
#    "insert into enFacetWorldRegions (id, region, subregion) values (?,?,?)", 
#    regionData)
#  dbConn.commit()
#
#
##### end ###
