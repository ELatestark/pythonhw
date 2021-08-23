#!/usr/bin/env python3
# get location and google maps link from coordinates
from geopy.geocoders import Nominatim
coordsfile = passwd_file = open('/etc/file.txt', 'r')
coordsfile_lines = coordsfile.readlines()
coords = [x.replace("'", "").replace('"', "").split(',') for x in coordsfile_lines[0].split(';')]
coords = [[int(coords[i][j])/60**j for j in range(len(coords[i]))] for i in range(2)]
place = Nominatim(user_agent='hw16').reverse((str(sum(coords[0])), str(sum(coords[1]))))
print(place)
print('https://www.google.com/maps/search/?api=1&query=' + str(sum(coords[0])) + ',' + str(sum(coords[1])))