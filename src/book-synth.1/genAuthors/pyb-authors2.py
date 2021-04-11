#Synthesize LaTeX author compilation from .bib and processed .aux
#Brygg Ullmer, Clemson University
#Begun 2021-02-27

#https://stackoverflow.com/questions/30768745/is-there-a-reliable-python-library-for-taking-a-bibtex-entry-and-outputting-it-i

from pybtex.database.input import bibtex
from pybtex import errors
import pandas as pd
import sys

errors.set_strict_mode(False)
parser = bibtex.Parser()
bib_data = parser.parse_file('tangibles-common6.bib')

citationsFn = 'citations4.txt'
citationsF  = open(citationsFn, 'r+t')
lines       = citationsF.readlines()
citations   = {}
for line in lines:
  cleanline = line.rstrip()
  citations[cleanline] = True

authors = {}

for el in bib_data.entries:
   bibref = str(el)
   #if bibref in citations:
   #  print('Y', bibref)
   #else:
   #  print('N', bibref)

   if bibref not in citations:
     continue # ignore non-cited articles

   persons = bib_data.entries[el].persons
   if 'author' in persons:
     authorList = persons['author']
     for author in authorList:
       #print('author', author)
       #strauthor = str(author[0])
       #if len(author)>1:
       #  strauthor += ', '
       #  strauthor += ' '.join(author[1:])
       strauthor = str(author)

       if strauthor not in authors:
         authors[strauthor] = []
       authors[strauthor].append(el)

print('''\addcontentsline{toc}{chapter}{Authors cited}
\multicolumn{2}{l l}{
\begin{tabular}{l l}''')


#print(len(authors))
#print(authors.keys())
#sys.exit(-1)

authorKeys  = authors.keys()
authorNames = sorted(authorKeys)

for author in authorNames:
  print(author + '&')
  cites = authors[author]
  print('\cite{' + ','.join(cites) + '}\\\\')

print('\end{tabular}')
 
### end ###
