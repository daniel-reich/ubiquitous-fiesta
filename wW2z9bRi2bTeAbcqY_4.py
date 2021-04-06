
def solve(a, b):
  k = 'b - 1'.replace('b', str(b))
  if a == b:
    return "Any number"
  try:
    return round(eval(k) / (a - 1), 3)
  except:
    return "No solution"

