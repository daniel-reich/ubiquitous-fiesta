
def side(a,b):
  x1,y1 = a
  x2,y2 = b
  return ((x2-x1)**2+(y2-y1)**2)**0.5
def perimeter(lst):
  A,B,C = lst
  return round(side(A,B)+side(B,C)+side(C,A),2)

