
def paths(x, y):
  if x == 0 or y == 0:
    return 1
  elif x == 1:
    return y + 1
  elif y == 1:
    return x + 1
  else:
    return paths(x-1,y) + paths(x,y-1)

