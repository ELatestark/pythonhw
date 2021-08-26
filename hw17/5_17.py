#!/usr/bin/env python3
# get exif location from photo and write to out_file
from exif import Image
with open('C:\etc\IMG.jpg', 'rb') as image_file:
    my_image = Image(image_file)
out_file = open('C:/etc/text.txt', 'w')
str_long = ','.join(map(str, my_image.gps_longitude))
str_lat = ','.join(map(str, my_image.gps_latitude))
out_file.write(str_lat + ";" + str_long)