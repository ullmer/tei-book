# Generate book thumbnails
# Brygg Ullmer, Clemson University
# Begun 2021-03-19

from PIL import Image, ImageDraw, ImageFont
from imgSupport import *
import sys

basedir     = '/home/bullmer/book/2021-03-17b/'
imageListFn = 'main12b.figs'
imageListF  = open(imageListFn, 'r+t')
rawlines    = imageListF.readlines()
outPrefix = 'thumbs/img' 
targetRes = [150, 300]
#targetRes = [250,250]

idx = 0
for rawline in rawlines:
  cleanline = rawline.rstrip()
  print('reading '+cleanline)
  imgFn = basedir + cleanline
  outFn = outPrefix + str(idx).zfill(3) + '.jpg'
  #resize_and_crop(imgFn, outFn, [250,250], crop_type='middle')
  idx += 1
  try:
    resize_and_crop(imgFn, outFn, targetRes, crop_type='middle')
  except:
    print("problem opening image" + cleanline)
    e = sys.exc_info()   #e = sys.exc_info()[0]
    print('error: '+str(e))

### end ###
