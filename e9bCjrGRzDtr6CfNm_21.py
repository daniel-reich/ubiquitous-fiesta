
def solve(a, b):
  if a == b:
    return 'Any number' if b == 3*a - 4 else 'No solution'
  else:
    return round((b - 3*a + 4) / (a - b), 3)

