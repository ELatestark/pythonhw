# !/usr/bin/env python3
# get location and google maps link from coordinates
from geopy.geocoders import Nominatim
coordsfile = passwd_file = open('/etc/file.txt', 'r')
coordsfile_lines = coordsfile.readlines()
coords = [x.replace("'", "").replace('"', "").split(',') for x in coordsfile_lines[0].split(';')]
c1, c2=0, 0
for i in range(len(coords[0])):
    c1+=int(coords[0][i])/60**i
for i in range(len(coords[1])):
    c2 += int(coords[1][i]) / 60 ** i
place = Nominatim(user_agent='hw16').reverse((c1, c2))
print(place)
print('https://www.google.com/maps/search/?api=1&query='+str(c1)+','+str(c2))