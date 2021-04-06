
def is_circle_collision(c1, c2):
  return abs(c1[1] - c2[1]) <= c1[0] and abs(c1[2] - c2[2]) <= c1[0]

