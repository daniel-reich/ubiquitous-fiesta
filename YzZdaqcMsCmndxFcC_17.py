
def centroid(x1, y1, x2, y2, x3, y3):
  try:
    if (x2-x1)/(y2-y1) == (x3-x2)/(y3-y2):
      return False
  except ZeroDivisionError:
    pass
  return (round((x1+x2+x3)/3,2), round((y1+y2+y3)/3,2))

