
def paths(x, y):
  if x > 0 and y > 0:
    return paths(x,y-1) + paths(x-1,y)
  if x > 0:
    return paths(x-1,y)
  if y > 0:
    return paths(x,y-1)
  else:
    return 1

