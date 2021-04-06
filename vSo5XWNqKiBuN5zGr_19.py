
def divide(x, y, k=0, i=0):
  if not k: k = [-1, 1][x*y > 0]
  if abs(x) < abs(y): return k * i
  return divide([x-y, x+y][x*y < 0], y, k, i+1)

