## File gathering support routines adopted from several external sources
# Aggregation by Brygg Ullmer, Clemson University
# Begun 2021-03-16

from PIL        import Image, ImageDraw, ImageFont, ImageOps
import PyPDF4
import io

############################################################
### from: https://stackoverflow.com/questions/47123649/pil-draw-transparent-text-on-top-of-an-image

def overlayText(sourceImg, targImg, text):

  image = Image.open("spongebob.gif").convert("RGBA")
  txt = Image.new('RGBA', image.size, (255,255,255,0))

  font = ImageFont.truetype("impact.ttf", 25)
  d = ImageDraw.Draw(txt)    

  d.text((0, 0), "This text should be 5% alpha", fill=(0, 0, 0, 15), font=font)
  combined = Image.alpha_composite(image, txt)    
  combined.save("foo.gif")


############################################################
### from: https://gist.github.com/sigilioso/2957026

def resize_and_crop(img_path, modified_path, size, crop_type='top'):
    """
    Resize and crop an image to fit the specified size.

    args:
    img_path:      path for the image to resize.
    modified_path: path to store the modified image.
    size:          `(width, height)` tuple.
    crop_type:     can be 'top', 'middle' or 'bottom', depending on this
      value, the image will cropped getting the 'top/left', 'middle' or
      'bottom/right' of the image to fit the size.
    raises:
    Exception:     if can not open the file in img_path of there is problems
      to save the image.
    ValueError:    if an invalid `crop_type` is provided.
    """
    # If height is higher we resize vertically, if not we resize horizontally
    img = Image.open(img_path)
    # Get current and desired ratio for the images
    img_ratio = img.size[0] / float(img.size[1])
    ratio = float(size[0]) / float(size[1])
    #The image is scaled/cropped vertically or horizontally depending on the ratio
    if ratio > img_ratio:
        img = img.resize((size[0], int(round(size[0] * img.size[1] / img.size[0]))),
            Image.ANTIALIAS)
        # Crop in the top, middle or bottom
        if crop_type == 'top':
          box = (0, 0, img.size[0], size[1])
        elif crop_type == 'middle':
          box = (0, int(round((img.size[1] - size[1]) / 2)), img.size[0],
                int(round((img.size[1] + size[1]) / 2)))
        elif crop_type == 'bottom':
          box = (0, img.size[1] - size[1], img.size[0], img.size[1])
        else :
          raise ValueError('ERROR: invalid value for crop_type')
        img = img.crop(box)
    elif ratio < img_ratio:
        img = img.resize((int(round(size[1] * img.size[0] / img.size[1])), size[1]),
            Image.ANTIALIAS)
        # Crop in the top, middle or bottom
        if crop_type == 'top':
          box = (0, 0, size[0], img.size[1])
        elif crop_type == 'middle':
          box = (int(round((img.size[0] - size[0]) / 2)), 0,
                int(round((img.size[0] + size[0]) / 2)), img.size[1])
        elif crop_type == 'bottom':
          box = (img.size[0] - size[0], 0, img.size[0], img.size[1])
        else :
          raise ValueError('ERROR: invalid value for crop_type')
        img = img.crop(box)
    else :
        img = img.resize((size[0], size[1]),
            Image.ANTIALIAS)
    # If the scale is the same, we do not need to crop
    img.save(modified_path)


############################################################
### Adopted from: https://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python/34116472#34116472 and 
### https://gist.github.com/jrsmith3/9947838 
#Also engaged:
#https://stackoverflow.com/questions/51048266/python-pil-cant-open-pdfs-for-some-reason

def convPdf2Jpg(srcFn, targFn):
  srcPDF  = PyPDF4.PdfFileReader(open(srcFn, "rb"), strict=False)
  page    = srcPDF.getPage(0)
  try:
    xobj    = page['/Resources']['/XObject'].getObject()
  except:
    print("convPdf2Jpg error probing page; ignoring "+srcFn)
    return

  for obj in xobj:
    if xobj[obj]['/Subtype'] == '/Image':
      size = (xobj[obj]['/Width'], xobj[obj]['/Height'])
      data = xobj[obj].getData()

      if xobj[obj]['/ColorSpace'] == '/DeviceRGB':
        mode = "RGB"
      else:
        mode = "P"

      if xobj[obj]['/Filter'] == '/FlateDecode':
        img = Image.frombytes(mode, size, data)
        img2 = ImageOps.invert(img)
        #img.save(obj[1:] + ".png")
        print("inverting")
        img2.save(targFn)
      elif xobj[obj]['/Filter'] == '/DCTDecode':
        #img = open(obj[1:] + ".jpg", "wb")
        img = Image.frombytes(mode, size, data)
        img2 = ImageOps.invert(img)
        img2.save(targFn)
        #img = open(targFn, "wb")
        #img.write(data)
        #img.close()
      elif xobj[obj]['/Filter'] == '/JPXDecode':
        #img = open(obj[1:] + ".jp2", "wb")
        img = Image.frombytes(mode, size, data)
        img2 = ImageOps.invert(img)
        img2.save(targFn)
        #img = open(targFn, "wb")
        #img.write(data)
        #img.close()

### end ###

