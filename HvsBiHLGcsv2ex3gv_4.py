
import math
def shortestDistance(txt):
  l = txt.split(',')
  dist = ((int(l[0]) - int(l[2]))**2 + (int(l[1]) - int(l[3]))**2)**0.5
  return round(dist,2)

