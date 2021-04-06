
def overlapping_rectangles(rect1, rect2):
  (x1, y1, w1, h1), (x2, y2, w2, h2) = rect1, rect2
  if x1+w1 < x2: return 0
  return (min(x1+w1,x2+w2)-max(x1, x2))*(min(y1+h1,y2+h2)-max(y1, y2))

