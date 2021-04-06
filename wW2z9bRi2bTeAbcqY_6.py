
def solve(a, b):
  n, m = b-1, a-1
  if not m:
    if not n:
      return 'Any number'
    else:
      return 'No solution'
  else:
    return round(n/m, 3)

