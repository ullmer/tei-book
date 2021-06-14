# Brygg Ullmer, Miriam Konkel, and Breanna Filipiak
# Support class for engaging periodic table of the elements

import json

#end prefix = Enodia Data 
  
######################################################################### 
#################### Enodia Data : Chemical Elements #################### 

class edElements:
  elementUrl  = 'https://github.com/Bowserinator/Periodic-Table-JSON.git'
  elementJson = 'periodic-table-lookup.json'

  elementData           = None
  elementFullnames      = None
  elementFullnameHash   = None
  elementSymbolHash     = None
  elementRowHash        = None
  elementColHash        = None
  elementTable          = None
  elementFullSymbolHash = None

  #################### load data ####################

  def loadData(self):
    elementF         = open(self.elementJson, 'r+t')
    self.elementData = json.load(elementF)

    els = self.getElementList()
  
  #################### constructor ####################

  def __init__(self):
    self.elementFullnameHash = {}
    self.loadData()
    self.buildSymbolCoordHash()

  #################### getElementList ####################

  def getElementList(self):
    if self.elementFullnames != None:
      return self.elementFullnames

    if self.elementData == None:
      self.loadData()

    self.elementFullnames = self.elementData["order"]
    return self.elementFullnames

  #################### getElementByFullname ####################

  def getElementByFullname(self, elementFullname):
    if self.elementData == None:
      self.loadData()

    if elementFullname in self.elementFullnameHash:
      result = self.elementFullnameHash[elementFullname]
      return result

    if elementFullname in self.elementData:
      self.elementFullnameHash[elementFullname] = self.elementData[elementFullname]
      return self.elementFullnameHash[elementFullname]

    return None # error message would be preferable

  #################### buildSymbolHash ####################

  def getElsByRow(self, targRow):
    if targRow not in self.elementRowHash:
      print("edElements: getElsByRow: targRow not in elementRowHash")
      return None

    els = self.elementRowHash[targRow]
    return els

  #################### buildSymbolHash ####################

  def buildSymbolCoordHash(self):
    elFullnames = self.getElementList()
    self.elementSymbolHash = {}
    self.elementRowHash    = {}
    self.elementColHash    = {}
    self.elementTable      = {} # to become 2D hash by integer index
    self.elementFullSymbolHash = {}

    for elFullname in elFullnames:
      elData = self.getElementByFullname(elFullname)
      elSymbol = elData["symbol"]
      xpos     = elData["xpos"]
      ypos     = elData["ypos"]

      self.elementSymbolHash[elSymbol]       = elFullname
      self.elementFullSymbolHash[elFullname] = elSymbol

      if ypos not in self.elementRowHash:
        self.elementRowHash[ypos] = []
      self.elementRowHash[ypos].append(elFullname)

      if xpos not in self.elementColHash:
        self.elementColHash[xpos] = []
      self.elementColHash[xpos].append(elFullname)

      if xpos not in self.elementTable:
        self.elementTable[xpos] = {}

      self.elementTable[xpos][ypos] = elFullname

  #################### getElementBySymbol####################

  def getElementByTableIdx(self, x, y):
    if self.elementTable == None:
      print("edElements getElementByTableIdx error: no elementTable")

    if x not in self.elementTable:    return None
    if y not in self.elementTable[x]: return None
    return self.elementTable[x][y]
  
  #################### get symbol by fullname ####################

  def getSymbolByFullname(self, fullname):
    if fullname in self.elementFullSymbolHash:
      return self.elementFullSymbolHash[fullname]
    return None

  #################### getElementBySymbol####################

  def getElementBySymbol(self, elementSymbol):
    if self.elementData == None:
      self.loadData()

    if elementFullname in self.elementFullnameHash:
      result = self.elementFullnameHash[elementFullname]
      return result

    if elementFullname in self.elementData:
      self.elementFullnameHash[elementFullname] = self.elementData[elementFullname]
      return self.elementFullnameHash[elementFullname]

    return None # error message would be preferable

  #################### get maximum table width (from double-hash) ####################

  def getMaxTableHeight(self):
    maxTableHeight = 0
    xkeys = self.elementTable.keys()
    for x in xkeys:
      ykeys = self.elementTable[x]
      ylen  = len(ykeys)
      if ylen > maxTableHeight: maxTableHeight = ylen
    return maxTableHeight
  
  #################### get maximum table width (from double-hash) ####################

  def getMaxTableWidth(self):
    maxTableWidth = 0
    xkeys = self.elementTable.keys()
    for x in xkeys:
      if x > maxTableWidth: maxTableWidth = x
    return maxTableWidth

  #################### get maximum table width (from double-hash) ####################

  def getTableDimensions(self):
    tableWidth  = self.getMaxTableWidth()
    tableHeight = self.getMaxTableHeight()
    return [tableWidth, tableHeight]

  #################### get maximum table width (from double-hash) ####################

  def getFullnameMatrix(self):
    tableDimensions = self.getTableDimensions()
  
    table = []
    for x in range(1,tableDimensions[0]):
      row = []
      for y in range(1,tableDimensions[1]):
        elFullname = self.getElementByTableIdx(x, y)
        row.append(elFullname)
      table.append(row)
    return table

  #################### get maximum table width (from double-hash) ####################

  def getSymbolMatrix(self):
    tableDimensions = self.getTableDimensions()
  
    table = []
    for x in range(1,tableDimensions[0]):
      row = []
      for y in range(1,tableDimensions[1]):
        elFullname = self.getElementByTableIdx(x, y)
        elSymbol   = self.getSymbolByFullname(elFullname)
        row.append(elSymbol)
      table.append(row)
    return table
      
############################################## 
#################### main #################### 

def main():
  ed = edElements()
  print(ed.getElementList())
  print(ed.getElementByFullname('aluminium'))
  print(ed.getElsByRow(2))
  print(ed.getTableDimensions())
  #print(ed.getFullnameMatrix())
  print(ed.getSymbolMatrix())

if __name__ == "__main__":
  main()

### end ###

