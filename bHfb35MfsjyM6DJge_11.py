
def route_diff(lst):
  x, y = 0, 0
  for i in lst:
      if i == "N":
          y += 1
      if i == "S":
          y -= 1
      if i == "E":
          x += 1
      if i == "W":
          x -= 1
  return len(lst) - (abs(x) + abs(y))

