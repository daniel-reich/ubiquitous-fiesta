
def solve(a, b):
  n, d = b - 3*a + 4, a - b
  if n == 0 and d == 0:
    return 'Any number'
  if d == 0: 
    return'No solution'
  return round(n / d, 3)

