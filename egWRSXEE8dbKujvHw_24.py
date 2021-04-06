
def is_circle_collision(c1, c2):
  d = ((c1[1] - c2[1])**2 + (c1[2] - c2[2])**2)
  ds2 = d**.5
  if ds2 == 0:
    return True
  l = ((c1[0])**2 - (c2[0])**2 + d) / (2 * ds2)
  return (c1[0] * c1[0]) - (l * l) >= 0

