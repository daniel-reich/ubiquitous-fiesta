
def solve(a, b):
  if a == b == 1: return 'Any number'
  if a == 1: return 'No solution'
  return round((b-1)/(a-1), 3)

