
def over_time(lst):
  n=min(lst[1],17)-max(lst[0],9)
  if n<0:n=0
  return '${:0.2f}'.format(Hround((((lst[1]-lst[0])%24-n)*lst[3]+n)*lst[2],2))
  
import math
def Hround(n, decimals=0):
  expoN = n * 10 ** decimals
  if abs(expoN) - abs(math.floor(expoN)) < 0.5:
    return math.floor(expoN) / 10 ** decimals
  return math.ceil(expoN) / 10 ** decimals

