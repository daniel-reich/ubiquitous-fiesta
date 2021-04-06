
def dist(p,q):
  [x1,y1],[x2,y2]=p,q
  return ((x1-x2)**2+(y1-y2)**2)**.5
def perimeter(lst):
  [p,q,r]=lst
  return round(dist(p,q)+dist(p,r)+dist(r,q),2)

