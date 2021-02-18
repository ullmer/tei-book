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
  processedRows = None
  row1Hash     = None
  row1Backhash = None
  row2Hash     = None

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

    self.row1Hash = {}; self.row2Hash = {}; self.row1Backhash = {}
    row1 = self.rows[0]; row2 = self.rows[1]
    idx = 0 
    for col in row1: #build map of columns in row 1
      if col not in self.row1Hash: 
        self.row1Hash[col] = []
      self.row1Hash[col].append(idx); idx += 1
      if col != None:
        self.row1Backhash[idx] = col

    idx = 0
    for col in row2: #repeat for row 2
      if col not in self.row2Hash: 
        self.row2Hash[col] = []
      self.row2Hash[col].append(idx); idx += 1

    #print("row1:" + str(self.row1Hash))
    #print("row2:" + str(self.row2Hash))

    return True
    
############### process rows ############### 

  def procRows(self):
    headerOk = self.procHeader()
    if headerOk == False:
      return False
    idx = 0
    self.processedRows = []
    for row in self.rows:
      if idx < 6:
        idx += 1; continue     #ignore header lines
      rowResult = self.procRow(row)
      if rowResult == False:
        sys.exit(-1)
      else:
        self.processedRows.append(rowResult)

############### process row ############### 

  def procRow(self, row):
    if self.row1Hash == None or self.row2Hash == None or self.row1Backhash == None:
      print("enTableSql: procRow called and row1Hash, row2Hash, or row1Backhash are None")
      return False
      
    #print("PR:", row)
    keys = self.row1Hash.keys()
    #print("k:", keys)

    vals = []; pairs = []
    for key in keys:
      if key == '':
        continue
      idx = self.row1Hash[key]
      val = row[idx[0]]
      pairs.append([key, val])
    #print(pairs)
    return(pairs)

############### process row ############### 

  def insertSqlRaw(self, dbFname):
    if self.processedRows == None:
      print("enTableSql: insertSqlRaw called but processedRows == None")
      return False
      
    print("raw student insertions")
    row1Keys = rows[0].keys()
    print("row1Keys:" + row1Keys)

    #for row in self.processedRows:

    dbConn   = sqlite3.connect(fbFname)
    dbCursor = dbConn.cursor()

    #dbCursor.executemany(
      "insert into enFacetWorldRegions (id, region, subregion) values (?,?,?)", 
    #regionData)
    #dbConn.commit()
      
############### constructor ############### 

  def __init__(self, filename):
    self.readCsvTable(filename)
    self.printTableDimensions()
    self.procRows()

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
