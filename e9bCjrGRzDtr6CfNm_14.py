
def solve(a, b):
  n, m = -3*a + b + 4, a-b
  if not m:
    if not n:
      return 'Any number'
    else:
      return 'No solution'
  else:
    return round(n/m, 3)

