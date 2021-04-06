
def right_triangle(x, y, z):
  if x<1 or y<1 or z<1:
    return False
  lst = [x*x,y*y,z*z]
  lst.sort()
  return lst[0] + lst[1] == lst[2]

