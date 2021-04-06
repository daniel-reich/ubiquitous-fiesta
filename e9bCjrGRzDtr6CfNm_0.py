
def solve(a, b):
  if a-b:
    return round((4-3*a+b)/(a-b),3)
  else:
    return 'No solution' if 4-3*a+b else 'Any number'

