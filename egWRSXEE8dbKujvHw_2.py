
def is_circle_collision(c1, c2):
  dist2 = (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2
  return (c1[0]+c2[0])**2 >= dist2

