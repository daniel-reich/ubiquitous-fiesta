
from math import ceil
def over_time(lst):
  start, end, rate, multi = lst[0], lst[1], lst[2], lst[3]
  normal = end - start if 17 - start > 0 and end < 17 else 17 - start
  normal = 0 if normal < 0 else normal
  over = end - start if start > 17 and  end - start > 0 else end - 17
  over = 0 if over < 0 else over
  return '${:0.2f}'.format(ceil((normal+over*multi)*rate*100)/100)

