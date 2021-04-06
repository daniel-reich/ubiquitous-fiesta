
import re
def is_odd(n):
  return 'Yes' if n^1==n-1 else 'No'
def is_even(n):
  return 'Yes' if any(bool(re.findall(i,n[-1])) for i in '02468') else 'No'

