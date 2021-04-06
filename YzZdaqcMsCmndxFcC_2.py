
def centroid(x1, y1, x2, y2, x3, y3):
  x = round((x1 + x2 + x3) / 3, 2)
  y = round((y1 + y2 + y3) / 3, 2)
  if x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2) == 0:
    return False
  return (x, y)

