
def list_operation(x, y, n):
  return [y for y in [x for x in range(x, y+1)] if y % n == 0]

