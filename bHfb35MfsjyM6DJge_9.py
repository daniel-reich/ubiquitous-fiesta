
def route_diff(directions):
  b = [0,0]
  for el in directions:
    if el == 'N':
      b[1] += 1
    if el == 'S':
      b[1] -= 1
    if el == 'W':
      b[0] += 1
    if el == 'E':
      b[0] -= 1
  return (len(directions) - (abs(b[0]) + abs(b[1])))

