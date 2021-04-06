
def solve(a, b):
  try:
    return round((b-1)/(a-1),3)
  except ZeroDivisionError:
    x = 93
    if eval('(a * x) + 1 == b + x') == True:
      return 'Any number'
    else:
      return 'No solution'

