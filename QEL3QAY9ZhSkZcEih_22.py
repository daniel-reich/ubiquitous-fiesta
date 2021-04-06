
import re
​
def is_odd(n):
  return 'Yes' if n & 1 else 'No'
​
def is_even(n):
  return 'Yes' if bool(re.search(r'[02468]$', n)) else 'No'

