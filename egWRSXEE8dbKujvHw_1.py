
def is_circle_collision(c1, c2):
  x = c1[1] - c2[1]
  y = c1[2] - c2[2]
  r = c1[0] + c2[0]
  
  return x**2 + y**2 < r**2

