
#Finds center of mass of centrifuge, if 0,0, it's balanced
import math
from itertools import combinations
def c_fuge(n,k):
  clist=(list(combinations([i for i in range(n)],k)))
  if clist==[()]:return False
  a=0;alist=[]
  angle=2*math.pi/n
  while a<2*math.pi:
    alist.append([math.sin(a),math.cos(a)])
    a+=angle
  for i in clist:
    x=0;y=0
    for j in i:
      y+=alist[j][0]
      x+=alist[j][1]
    if abs(x/k)<.001 and abs(y/k)<.001:
      return True
  return False

