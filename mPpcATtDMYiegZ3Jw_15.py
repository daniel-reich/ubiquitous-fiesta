
def right_triangle(x, y, z):
  return sorted([x,y,z])[0]**2+sorted([x,y,z])[1]**2 == sorted([x,y,z])[2]**2 if (x>0 and y>0 and z>0) else False

