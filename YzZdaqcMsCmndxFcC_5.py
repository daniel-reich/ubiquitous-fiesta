
def centroid(x1, y1, x2, y2, x3, y3):
  import math
  a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
  b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
  c = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
  case = triangle(a, b, c)
  if case:
    x = round((x1 + x2 + x3) / 3, 2)
    y = round((y1 + y2 + y3) / 3, 2)
    tup = (x,y)
    return tup
  else:
    return False
    
def triangle(a, b, c):
  if a + b == c:
    return False
  else:
    return True

