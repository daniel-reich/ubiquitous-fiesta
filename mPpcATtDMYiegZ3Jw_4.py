
def right_triangle(x, y, z):
  s = sorted([x,y,z])
  return all(i>0 for i in s) and s[2]**2 == s[0]**2 + s[1]**2

