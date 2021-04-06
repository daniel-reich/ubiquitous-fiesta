
def mag2(p1, p2):
  return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
​
def is_rectangle(coordinates):
  coords = [[int(x) for x in coord.strip('(').strip(')').split(',')] for coord in coordinates]
  if len(coords) < 4:
    return False
  return mag2(coords[0], coords[1]) == mag2(coords[2], coords[3]) and \
    mag2(coords[1], coords[2]) == mag2(coords[3], coords[0]) and \
    (coords[0][1] - coords[1][1]) * (coords[1][1] - coords[2][1]) == \
    (coords[1][0] - coords[2][0]) * (coords[1][0] - coords[0][0])

