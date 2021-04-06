
import math
def shortestDistance(txt):
  txt = txt.split(',')
  for i in txt:
    txt[txt.index(i)] = int(txt[txt.index(i)])
  return round(math.sqrt((txt[0]-txt[2])**2+(txt[1]-txt[3])**2),2)

