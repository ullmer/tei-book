#Synthesize LaTeX year compilation from .bib and processed .aux
#Brygg Ullmer, Clemson University
#Begun 2021-02-28

#https://stackoverflow.com/questions/30768745/is-there-a-reliable-python-library-for-taking-a-bibtex-entry-and-outputting-it-i

from pybtex.database.input import bibtex
from pybtex import errors
import pandas as pd
import sys

errors.set_strict_mode(False)
parser = bibtex.Parser()
bib_data = parser.parse_file('tangibles-common8.bib')

citationsFn = 'citations4.txt'
citationsF  = open(citationsFn, 'r+t')
lines       = citationsF.readlines()
citations   = {}
for line in lines:
  cleanline = line.rstrip()
  citations[cleanline] = True

authors = {}
yearHash = {}

for el in bib_data.entries:
   bibref = str(el)

   if bibref not in citations:
     continue # ignore non-cited articles

   fields = bib_data.entries[el].fields
   if 'year' in fields:
     #print(el, fields['year'])
     year = int(fields['year'])
     if year not in yearHash:
       yearHash[year] = []
     yearHash[year].append(el)

#print(yearHash)
years = sorted(yearHash.keys())

#################### chunkList ####################

def chunklist(list, chunksize):
  n = chunksize; l = list
  # using list comprehension   # https://www.geeksforgeeks.org/break-list-chunks-size-n-python/
  result = [l[i:i + n] for i in range(0, len(l), n)]  
  return result

#################### renderBatch ####################

def renderBatch(headline, articles):
  print(str(year) + '\n')
  print('\\begin{longtable}{p{2in}p{2in}p{2in}}')
  sortedArt = sorted(articles, key=str.lower)
  chunkedArt = chunklist(sortedArt, 3)
  for chunk in chunkedArt:
    citedChunk = [] 
    for art in chunk:
      citedChunk.append('\cite{' + art + '}')
    outstr = '&'.join(citedChunk) + ' \\\\'
    print(outstr)
  print('\\end{longtable}');

#################### main ####################

yearGrouping = {1700: [1727, 1751], 1800: [1825, 1845, 1852, 1884, 1890], 1900: [1903], 
                1910: [1911, 1912], 1920: [1927], 1930: [1931, 1932, 1936, 1937, 1938], 
                1950: [1952, 1957], 1960: [1960, 1962], 1970: [], 1980:[], 1990: [], 2000: [], 2010: [], 2020: []}

for decade in [1970, 1980, 1990, 2000, 2010, 2020]:
  for y in range(10):
    year = decade + y
    if year in yearHash:
      yearGrouping[decade].append(year)
#print(yearGrouping)

for decade in yearGrouping:
  print('\\hrule \\section{' + str(decade) + '}')
  articles = []
  for year in yearGrouping[decade]:
    articlesInYear = yearHash[year]
    articles += articlesInYear
    if year >= 1990:
      renderBatch(year, articles)
      articles = []
  if year < 1990:
    renderBatch(decade, articles)
    articles = []

### end ###

