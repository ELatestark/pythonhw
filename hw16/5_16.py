#!/usr/bin/env python3
# get location and google maps link from coordinates
import re
from geopy.geocoders import Nominatim
coordsfile = open('text.txt', 'r')
coordsfile_lines = coordsfile.readlines()
coords_list = list(re.sub('[^0-9\.]', ' ', str(coordsfile_lines)).strip().split(" "))
coords = [coords_list[:len(coords_list)//2],coords_list[len(coords_list)//2:]]
coords = [[float(coords[i][j])/60**j for j in range(len(coords[i]))] for i in range(2)]
place = Nominatim(user_agent='hw16').reverse((str(sum(coords[0])), str(sum(coords[1]))))
print(place)
print('https://www.google.com/maps/search/?api=1&query=' + str(sum(coords[0])) + ',' + str(sum(coords[1])))