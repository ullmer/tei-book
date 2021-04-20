import json
sdgF = open('en-unsdg-list.json', 'r+t')
sdgD = json.load(sdgF)
sdgH = {}

for sdg in sdgD:
  code = sdg["code"]; title = sdg["title"]
  print(code, title)

def tr(text): print("<tr>{}</tr>".format(text), end='')

#for i in range(26): print("<tr>{} : {} : {}</td>".format(chr(i+65),i%16+1,sdg[i]))
