
def same_line(lst):
​
  x1, y1 = lst[0][0], lst[0][-1]
  x2, y2 = lst[1][0], lst[1][-1]
  x3, y3 = lst[2][0], lst[2][-1]
​
  try:
    slope1 = (y2 - y1) / (x2 - x1)
  except ZeroDivisionError:
    slope1 = 'und'
  
  try:
    slope2 = (y3 - y2) / (x3 - x2)
  except ZeroDivisionError:
    slope2 = 'und'
​
  x = round((x1 + x2 + x3) / 3, 2)
  y = round((y1 + y2 + y3) / 3, 2)
​
  if slope1 == slope2:
    return True
  return False

