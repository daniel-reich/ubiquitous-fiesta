
def number_of_days(coordinate):
  x, y = coordinate
  d = abs(x) + abs(y)
  return d+d//5-1 if d % 5 == 0 else d+d//5

