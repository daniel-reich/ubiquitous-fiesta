
def solve(a, b):
  try:
    if a == 2 and b == 2:
      return 'Any number'
    return round((b - 3*a + 4) / (a - b),3)
  except:
    return 'No solution'

