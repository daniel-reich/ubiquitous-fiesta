
def solve(a, b):
  return ('Any number' if a is 1 and b is 1 else 
    'No solution' if a is 1 else 
    round((b - 1) / (a - 1), 3))

