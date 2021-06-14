# Brygg Ullmer, Miriam Konkel, and Breanna Filipiak
# Support class for engaging periodic table of the elements

import json

#end prefix = Enodia Data 
  
#################### Enodia Data : Chemical Elements #################### 

class endElements:
  sourceUrl  = 'https://github.com/Bowserinator/Periodic-Table-JSON.git'
  sourceJson = 'periodic-table-lookup.json'
  sourceD    = None

  #################### load data ####################

  def loadData(self):
    json.load(self.sourceD)

### end ###

