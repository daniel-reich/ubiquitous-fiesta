
def centroid(x1, y1, x2, y2, x3, y3):
  if x2*y3-y2*x3 -(x1*y3-y1*x3) + x1*y2-x2*y1==0: return False
  x =(x1+x2+x3)/3
  y = (y1 + y2+y3)/3
  return (round(x,2),round(y,2))

