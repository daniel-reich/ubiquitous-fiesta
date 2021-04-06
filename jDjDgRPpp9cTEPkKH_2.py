
def over_time(lst):
  s,e,h,o = lst
  if s>17 and e>17:
    d = abs(s-e)
    return '${:,.2f}'.format(normal_round(d*(h*o),2))
  else:
    if e>17:  over = e-17
    else: over=0
    d = abs(s-(e-over))
    return '${:,.2f}'.format(normal_round(h*d + over*(h*o),2))
  
def normal_round(n, decimals=0):
  import math
  expoN = n * 10 ** decimals
  if abs(expoN) - abs(math.floor(expoN)) < 0.5:
    return math.floor(expoN) / 10 ** decimals
  return math.ceil(expoN) / 10 ** decimals

