
def solve(a, b):
  if a == b:
    return "Any number" if a == 2 else "No solution"
  else:
    return round((-3 * a + b + 4) / (a - b), 3)

