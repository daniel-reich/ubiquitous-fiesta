
def solve(a, b):
​
  try:
    return round(eval('((-3*a) + (4+b))/(a-b)'),3)
  except ZeroDivisionError:
    x = 93
    if eval('(a*x)-b == (b*x)-(3*a)+4') == True:
      return 'Any number'
    else:
      return 'No solution'

