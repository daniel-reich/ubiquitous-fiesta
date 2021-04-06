
def centroid(x1, y1, x2, y2, x3, y3):
  if x1 < 0:
    return False
  else:
    return (round(((x1 + x2 + x3) / 3),2),round(((y1 + y2 + y3) / 3),2))

