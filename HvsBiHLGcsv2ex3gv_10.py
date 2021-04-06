
import math
def shortestDistance(txt):
  txt1 = txt.split(",")
  return round(math.sqrt(pow((int(txt1[0])- int(txt1[2])), 2) + pow((int(txt1[1])- int(txt1[3])), 2)), 2)

