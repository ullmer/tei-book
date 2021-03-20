# Generate book thumbnails
# Brygg Ullmer, Clemson University
# Begun 2021-03-19

from PIL import Image, ImageDraw, ImageFont
from pilSupport import *
import sys

basedir     = '/home/bullmer/book/2021-03-17b/'
imageListFn = 'main12b.figs'
imageListF  = open(imageListFn, 'r+t')
rawlines    = imageListF.readlines()
outPrefix = 'thumbs/img' 

idx = 0
for rawline in rawlines:
  cleanline = rawline.rstrip()
  print('reading '+cleanline)
  imgFn = basedir + cleanline
  outFn = outPrefix + str(idx).zfill(3) + '.png'
  resize_and_crop(imgFn, outFn, [250,250], crop_type='middle')
  try:
    #image = Image.open(imgFn)
    #w,h= image.size
    #print(cleanline,w,h)
    #image.close()
    resize_and_crop(imgFn, outFn, 250, crop_type='middle')
  except:
    print("problem opening image" + cleanline)
    e = sys.exc_info()   #e = sys.exc_info()[0]
    print('error: '+str(e))

### end ###
