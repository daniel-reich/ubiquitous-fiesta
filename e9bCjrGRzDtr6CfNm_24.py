
def solve(a, b):
  try:
    n=(-(3*a)+4+b)
    d=(a-b)
    x=n/d
    return round(x,3)
  except ZeroDivisionError:
    if n==0:
      return 'Any number'
    else: 
      return 'No solution'

