
def same_line(lst):
  x1, y1, x2, y2, x3, y3 = (i for j in lst for i in j)
  return (x1-x2)*(y1-y3) == (x1-x3)*(y1-y2)

