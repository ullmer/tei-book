# Generate book thumbnails
# Brygg Ullmer, Clemson University
# Begun 2021-03-19

from PIL import Image, ImageDraw, ImageFont
from imgSupport import *
import sys

basedir     = '/home/bullmer/book/2021-03-17b/'
imageListFn = 'main12b.figs'
tmpFn       = 'temp.jpg'
imageListF  = open(imageListFn, 'r+t')
rawlines    = imageListF.readlines()
outPrefix = 'thumbs/img' 
targetRes = [150, 300]
#targetRes = [250,250]

idx = 0
for rawline in rawlines:
  cleanline = rawline.rstrip()
  extension = cleanline[-3:]
  imgFn = basedir + cleanline

  print('reading '+extension)
  if extension == 'pdf':
    print(imgFn)
    convPdf2Jpg(imgFn, tmpFn)
  else:
    idx += 1
    continue

  outFn = outPrefix + str(idx).zfill(3) + '.jpg'
  idx += 1
  try:
    resize_and_crop(tmpFn, outFn, targetRes, crop_type='middle')
    pass
  except:
    print("problem opening image" + cleanline)
    e = sys.exc_info()   #e = sys.exc_info()[0]
    print('error: '+str(e))

### end ###
