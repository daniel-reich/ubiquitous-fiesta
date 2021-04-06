
def solve(a, b):
  if a - 1 == 0 and b - 1 == 0:
    return 'Any number'
  if a - 1 == 0:
    return 'No solution'
  return round((b - 1) / (a - 1), 3)

