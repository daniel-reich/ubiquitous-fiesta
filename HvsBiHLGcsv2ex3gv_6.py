
import math
def shortestDistance(txt):
 l = [int(s) for s in txt.split(',')]
 distance = math.sqrt( ((l[0]-l[2])**2)+((l[1]-l[3])**2) )
 return round(distance, 2)

