# Brygg Ullmer, Miriam Konkel, and Breanna Filipiak
# Support class for engaging periodic table of the elements

import json

#end prefix = Enodia Data 
  
######################################################################### 
#################### Enodia Data : Chemical Elements #################### 

class edElements:
  elementUrl  = 'https://github.com/Bowserinator/Periodic-Table-JSON.git'
  elementJson = 'periodic-table-lookup.json'

  elementData         = None
  elementFullnames    = None
  elementFullnameHash = None
  elementSymbolHash   = None
  elementRowHash      = None
  elementColHash      = None

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

    for elFullname in elFullnames:
      elData = self.getElementByFullname(elFullname)
      elSymbol = elData["symbol"]
      xpos     = elData["xpos"]
      ypos     = elData["ypos"]

      self.elementSymbolHash[elSymbol] = elFullname

      if ypos not in self.elementRowHash:
        self.elementRowHash[ypos] = []
      self.elementRowHash[ypos].append(elFullname)

      if xpos not in self.elementColHash:
        self.elementColHash[xpos] = []
      self.elementColHash[xpos].append(elFullname)

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

############################################## 
#################### main #################### 

def main():
  ed = edElements()
  print(ed.getElementList())
  print(ed.getElementByFullname('aluminium'))
  print(ed.getElsByRow(2))

if __name__ == "__main__":
  main()

### end ###

