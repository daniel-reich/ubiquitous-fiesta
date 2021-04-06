
import math
def same_line(lst):
  a,b,c = lst
  ax,ay,bx,by,cx,cy = a[0],a[1],b[0],b[1],c[0],c[1]
  ab = math.sqrt((by-ay)**2 + (bx-ax)**2)
  ac = math.sqrt((cy-ay)**2 + (cx-ax)**2)
  bc = math.sqrt((cy-by)**2 + (cx-bx)**2)
  dist = [ab,ac,bc]
  s = 0
  for a in dist:
    if a != max(dist):
      s+=a
  return abs(s  - max(dist)) < 0.01

