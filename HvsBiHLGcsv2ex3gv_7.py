
import math
def shortestDistance(txt):
  lst = txt.split(',')
  return round(math.sqrt(math.pow(int(lst[0]) - int(lst[2]),2) + math.pow(int(lst[1]) - int(lst[3]),2)),2)

