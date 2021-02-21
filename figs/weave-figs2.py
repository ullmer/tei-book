# weave figure subpaths
# brygg ullmer
# begun 2021-02-20

import glob, os, sys, yaml

chapters = ['foreword', 'intro']
for i in range(1,10):
  chapters.append('ch' + str(i))
chapters.append('appdx')
print(chapters)

subdirsY  = \
  '[enodia,figs,figures,img_c4,img_c7,img_c8,vign,webCompanion]'
ssubdirsY = \
  '[enodia,img,NewImages,tei-crap,toolkit-imgs]'

subdirs  = yaml.safe_load(subdirsY)
ssubdirs = yaml.safe_load(ssubdirsY)
print(subdirs)
print(ssubdirs)

def tweakPath(path):
  idx    = path.find('/')
  twpath = path[idx+1:]
  return twpath

for chapter in chapters:
  if not os.path.exists(chapter):
    print('error: chapter ' + chapter + ' does not exist')
    continue

  print('='*50); print(chapter)
  childrenForConsideration = []

  for subdir in subdirs:
    sub = chapter + '/' + subdir
    if os.path.exists(subdir):
      globpat = sub + '/*'
      #print(globpat)

      try:
        subels = glob.glob(globpat)
	childrenForConsideration += subels
      except: 
        print('glob error processing '+chapter)
	e = sys.exc_info()   #e = sys.exc_info()[0]
	print('error: '+str(e))

  #special consideration for "figs", with frequent subdirs; 
  # "figures" symlinked to "figs"

  for ssubdirRel in ssubdirs:
    ssubdir = chapter + '/figs/' + ssubdirRel
    if os.path.exists(ssubdir) and os.path.isdir(ssubdir):
      globpat = ssubdir + '/*'
      subels = glob.glob(globpat)
      childrenForConsideration += subels

  #print(childrenForConsideration)
  for child in childrenForConsideration:
    twchild = tweakPath(child)
    #if not os.path.exists(twchild): #if symlink not already cast
    if True:
      try:
        os.remove(twchild)
        os.symlink("../" + child, twchild)
        #print(child, twchild)
      except:
        print('symlink error processing', child, twchild)
	e = sys.exc_info()   #e = sys.exc_info()[0]
	print('error: '+str(e))
      #print('symlink:', child, twchild)

### end ###
