
def right_triangle(x, y, z):
  lst = sorted([x,y,z])
  if all(a>0 for a in lst):
    return lst[-1]**2 == sum(a**2 for a in lst[:-1])
  return False

