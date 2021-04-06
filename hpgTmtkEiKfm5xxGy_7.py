
def paths(x, y):
  x,y = abs(x), abs(y)
  if (x,y) == (0,0):
    return 1
  total = 0
  if x > 0:
    total += paths(x-1, y)
  if y > 0:
    total += paths(x, y-1)
  return total

