#!/usr/bin/env python3
# get thumbnail of photo
from PIL import Image, ImageOps

img = Image.open('IMG.jpg')
percentage = int(input('Insert desired resize ratio in percentage (Valid input is integers from 1 to 99):'))
img.thumbnail((round(img.size[0] / 100 * percentage), round(img.size[1] / 100 * percentage)))
img_orientation = ImageOps.exif_transpose(img)
img_orientation.save(f'thumbnail-{percentage}.jpg')
