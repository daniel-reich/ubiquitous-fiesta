
def overlapping_rectangles(r1, r2):
  x0 = max(r1[0],r2[0])
  x1 = min(r1[0]+r1[2],r2[0]+r2[2])
  y0 = max(r1[1],r2[1])
  y1 = min(r1[1]+r1[3],r2[1]+r2[3])
  return max(x1-x0,0)*max(y1-y0,0)

