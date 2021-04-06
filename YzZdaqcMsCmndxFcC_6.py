
def invalid(x1,y1,x2,y2,x3,y3):
  try:
    return y1/x1 == y2/x2 and y1/x1 == y3/x3
  except ZeroDivisionError:
    return False
​
def centroid(x1, y1, x2, y2, x3, y3):
  if invalid(x1,y1,x2,y2,x3,y3):
    return False
  else:
    sumx = x1 + x2 + x3
    sumy = y1 + y2 + y3
    return (round(sumx/3,2),round(sumy/3,2))

