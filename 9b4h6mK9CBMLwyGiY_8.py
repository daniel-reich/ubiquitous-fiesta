
from math import sqrt
def get_distance(a, b):
  a = str(a)
  t1 = a.find(':')
  t2 = a.find(',')
  t3 = a.rfind(':')
  t4 = a.find('}')
  x1 = int(a[t1+1:t2])
  y1 = int(a[t3+1:t4])
  b = str(b)
  t1 = b.find(':')
  t2 = b.find(',')
  t3 = b.rfind(':')
  t4 = b.find('}')
  x2 = int(b[t1+1:t2])
  y2 = int(b[t3+1:t4])
  r = sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
  return(round(r,3))

