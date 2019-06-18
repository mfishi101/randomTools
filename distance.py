#!/usr/bin/env python -S -OO

from sys import argv, exit
from math import sin, cos, asin, sqrt, radians

if len(argv) != 5:
  print("Usage: distance lat1 lon1 lat2 lon2")
  exit(1)

lat1 = float(argv[1].strip().strip(','))
lon1 = float(argv[2].strip().strip(','))
lat2 = float(argv[3].strip().strip(','))
lon2 = float(argv[4].strip().strip(','))

print(6372.8 * 2 * asin(sqrt(sin(radians(lat2 - lat1) / 2)**2 + sin(radians(lon2 - lon1) / 2)**2 * cos(radians(lat1)) * cos(radians(lat2)))))
