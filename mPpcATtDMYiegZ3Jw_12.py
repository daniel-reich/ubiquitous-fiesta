
def right_triangle(x, y, z):
  a = sorted([x,y,z])
  if a[0] <= 0: return False
  return a[0]**2 + a[1]**2 == a[2]**2

