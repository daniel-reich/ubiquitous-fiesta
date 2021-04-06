
def is_parallelogram(lst):
  x1, x2, x3, x4 = lst[0][0], lst[1][0], lst[2][0], lst[3][0]
  y1, y2, y3, y4 = lst[0][1], lst[1][1], lst[2][1], lst[3][1]
  return  (x2-x1==x3-x4 and y2-y1==y3-y4) or (x3-x1==x2-x4 and y3-y1==y2-y4) or\
  (x3-x1==x4-x2 and y3-y1==y4-y2)

