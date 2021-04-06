
def same_line(lst):
  (x1, y1), (x2, y2), (x3, y3) = lst
  try:
    if x1 == x2 == x3 or y1 == y2 == y3:
      return True
    return (x1 - x2)/(y1 - y2) == (x2 - x3)/(y2 - y3)
  except ZeroDivisionError:
    return False

