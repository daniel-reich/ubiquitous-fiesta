
def right_triangle(x, y, z):
  if x>0 and y>0 and z>0:
    return (x*x + y*y + z*z) - max(x,y,z)**2 == max(x,y,z)**2
  return False

