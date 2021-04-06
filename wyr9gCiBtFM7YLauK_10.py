
from itertools import *
from operator import *
def time_sum(times):
  if not times: return 3*[0]
  h, m, s = list(map(sum, zip(*[(int(i) for i in t.split(':')) for t in times])))
  ds, z = divmod(0, 60)
  dm, s = divmod(s+ds, 60)
  dh, m = divmod(m+dm, 60)
  return [h+dh, m, s]

