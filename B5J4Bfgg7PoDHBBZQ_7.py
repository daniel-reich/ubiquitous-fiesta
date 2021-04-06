
def within_triangle(p1, p2, p3, test):
  return area(p1,p2,p3) == (area(p1,p2,test)+area(p1,p3,test)+area(p2,p3,test))
  
def area(a,b,c):
  x1,y1 = a
  x2,y2 = b
  x3,y3 = c
  return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2)

