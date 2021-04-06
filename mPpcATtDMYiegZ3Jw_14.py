
def right_triangle(a, b, c):
  r = sorted([a,b,c])
  return False if any(i<=0 for i in r) else r[-1]**2 == (r[0])**2+(r[1])**2

