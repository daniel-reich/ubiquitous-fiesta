
def is_rectangle(coordinates):
  x = 0
  y = 1
  coords = list(map(lambda x: tuple(map(lambda y: abs(y),eval(x))), coordinates))
  if len(coords) < 4:
    return False
  return (abs(coords[0][x]) == abs(coords[1][x]) and 
          coords[1][y] == coords[2][y] and 
          coords[2][x] == coords[3][x])

