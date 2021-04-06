
def centroid(x1, y1, x2, y2, x3, y3):
  from math import sqrt
  # check triangle
  sa = round(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 2)
  sb = round(sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2), 2)
  sc = round(sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2), 2)
  if sc > sa + sb or sb > sa + sc or sa > sb + sc:
    return False
  return round((x1 + x2 + x3) / 3, 2), round((y1 + y2 + y3) / 3, 2)

