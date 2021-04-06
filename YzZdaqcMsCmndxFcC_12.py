
import math
def centroid(ax, ay, bx, by, cx, cy):
  ab = round(math.sqrt((bx - ax) ** 2 + (by - ay) ** 2), 1)
  ac = round(math.sqrt((cx - ax) ** 2 + (cy - ay) ** 2), 1)
  bc = round(math.sqrt((cx - bx) ** 2 + (cy - by) ** 2), 1)
  if ab == ac + bc or ac == ab + bc or bc == ab + ac:
    return False
  return (round((ax+bx+cx)/3,2),round((ay+by+cy)/3,2))

