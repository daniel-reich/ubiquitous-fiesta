
def overlapping_rectangles(r1, r2):
  return max(min(r1[0]+r1[2],r2[0]+r2[2])-max(r1[0],r2[0]),0)*max(min(r1[1]+r1[3],r2[1]+r2[3])-max(r1[1],r2[1]),0)

