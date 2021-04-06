
def solve(a, b):
  try:
    return round((b-1)/(a-1),3) if a!=b else 'Any number'
  except ZeroDivisionError:
    return 'No solution'

