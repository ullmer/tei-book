# Brygg Ullmer, Miriam Konkel, and Breanna Filipiak
# Support class for engaging periodic table of the elements

import json

#end prefix = Enodia Data 
  
#################### Enodia Data : Chemical Elements #################### 

class endElements:
  elementUrl  = 'https://github.com/Bowserinator/Periodic-Table-JSON.git'
  elementJson = 'periodic-table-lookup.json'
  elementData = None

  #################### load data ####################

  def loadData(self):
    elementF         = open(self.elementJson, 'r+t')
    self.elementData = json.load(self.elementD)

### end ###

