
def route_diff(directions):
  x = 0
  y = 0
  for direct in directions:
    if direct == 'N':
      y += 1
    elif direct == 'S':
      y -= 1
    elif direct == 'E':
      x += 1
    elif direct == 'W':
      x -= 1
  minSteps = abs(x) + abs(y)
  yourSteps = len(directions)
  return yourSteps - minSteps

