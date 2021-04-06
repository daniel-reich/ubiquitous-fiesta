
def overlapping_rectangles(rect1, rect2):
  coor1 = get_coor(rect1)
  coor2 = get_coor(rect2)
  x1,y1 = max(coor1[0][0],coor2[0][0]),max(coor1[0][1],coor2[0][1])
  x2 = min(coor1[1][0],coor2[1][0])
  y2 = min(coor1[2][1],coor2[2][1])
  if x1>x2 or y1>y2:
    return 0
  width = x2-x1
  height = y2-y1
  return width*height
  
def get_coor(lst):
  x,y,w,h = lst
  return [(x,y),(x+w,y),(x,y+h),(x+w,y+h)]

