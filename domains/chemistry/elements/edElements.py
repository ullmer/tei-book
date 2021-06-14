# Brygg Ullmer, Miriam Konkel, and Breanna Filipiak
# Support class for engaging periodic table of the elements

import json

#end prefix = Enodia Data 
  
######################################################################### 
#################### Enodia Data : Chemical Elements #################### 

class endElements:
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

  #################### buildSymbolHash ####################

  def buildSymbolCoordHash(self):
    elFullnames = self.getElementList()
    elementSymbolHash = {}
    elementRowHash    = {}
    elementColHash    = {}

    for elFullname in elFullnames:
      elData = getElementByFullname(elFullname)
      symbol = elData["symbol"]
      xpos   = elData["xpos"]
      ypos   = elData["ypos"]

      self.elementSymbolHash[symbol] = elFullname

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
  ee = endElements()
  print(ee.getElementList())
  print(ee.getElementByFullname('aluminium'))

if __name__ == "__main__":
  main()

### end ###

