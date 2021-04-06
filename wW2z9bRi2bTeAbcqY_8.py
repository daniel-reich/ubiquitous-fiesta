
def solve(a, b):
  if a == 1:
    if b == 1:
      return 'Any number'
    return 'No solution'
  return round((b-1) / (a-1),3)

