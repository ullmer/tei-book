import json
sdgF = open('en-unsdg-list.json', 'r+t')
sdgD = json.load(sdgF)
sdgH = {}

for sdg in sdgD:
  code = sdg["code"]; title = sdg["title"]
  sdgH[code] = title

def td(text):     return "<td>{}</td>".format(text)

def sdgUrl(goal): return "<a href=https://en.wikipedia.org/wiki/Sustainable_Development_Goal_" + str(goal) + ">"

for i in range(26): 
  letter = chr(i+65); sdgN = i%16+1; sdgNC = str(sdgN)
  a = td(letter);  b = td(sdgUrl(sdgN) + str(sdgN) + "</a>"); c = td(sdgH[sdgNC])
  print("<tr>{} {} {}</tr>".format(a,b,c))

### end ###
