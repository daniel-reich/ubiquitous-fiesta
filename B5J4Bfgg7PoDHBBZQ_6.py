
def within_triangle(p1, p2, p3, test):
  x,y,x1,y1,x2,y2,x3,y3 = test[0],test[1],p1[0],p1[1],p2[0],p2[1],p3[0],p3[1]
  a = ((y2 - y3)*(x - x3) + (x3 - x2)*(y - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
  b = ((y3 - y1)*(x - x3) + (x1 - x3)*(y - y3)) / ((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
  c = 1 - a - b
  return (a >=0 and a<=1 and b>=0 and b<=1 and c>=0 and c<=1)

