
def overlapping_rectangles(rect1, rect2):
  xl = max(rect1[0], rect2[0])
  xr = min(rect1[0]+rect1[2], rect2[0]+rect2[2])
  yl = max(rect1[1], rect2[1])
  yh = min(rect1[1]+rect1[3], rect2[1]+rect2[3])
  if xl>=xr or yl >= yh:
    return 0
  else:
    return (xr-xl)*(yh-yl)

