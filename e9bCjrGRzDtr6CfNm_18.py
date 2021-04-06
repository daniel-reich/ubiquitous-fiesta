
def solve(a, b):
  u=(b-3*a+4)
  v=(a-b)
  if u == 0 and v == 0:
    return 'Any number'
  elif a == b:
    return 'No solution'
  return round(u/v, 3)

