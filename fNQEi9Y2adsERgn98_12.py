
def perimeter(lst):
  a,b,c = lst
  ret = dist(a,b)
  ret += dist(b,c)
  ret += dist(a,c)
  return round(ret,2)
  
def dist(a,b):
  x1,y1 = a
  x2,y2 = b
  return ((x2-x1)**2+(y2-y1)**2)**(1/2)

