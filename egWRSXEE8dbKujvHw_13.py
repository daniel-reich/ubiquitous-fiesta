
def is_circle_collision(c1, c2):
  distance = ((c1[1]-c2[1])**2 + (c1[2]-c2[2])**2)**0.5
  return True if distance <= c1[0] + c2[0] else False

