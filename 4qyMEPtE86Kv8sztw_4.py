
from fractions import Fraction
​
def binary_sum(lst):
  x, y = convert_to_float(lst[0].strip('0')), convert_to_float(lst[1].strip('0'))
  t = str(x+y)
  n = t.index('.')
​
  i, d = int(t[:n]), Fraction(t[n:])
  if not d:
    return str(i)
  elif not i:
    return str(d)
  else:
    return '{} {}'.format(i, d)
​
def convert_to_float(n):
  i, d = n.split('.')
  i = int(i,2) if i else 0
  d = int('0'+d,2)/2**(len(d)) if d else 0
  return float(i+d)

