
def overlapping_rectangles(rect1, rect2):
  width = min(rect1[0]+rect1[2],rect2[0]+rect2[2]) - max(rect1[0],rect2[0])
  height = min(rect1[1]+rect1[3],rect2[1]+rect2[3]) - max(rect1[1],rect2[1])
  if width > 0 and height > 0:
    return width * height
  return 0

