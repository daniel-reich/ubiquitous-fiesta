
def is_odd(n):
  return ['No', 'Yes'][n & 1] 
​
import re
def is_even(n):
  return 'Yes' if re.match(r'^-?\d*[02468]$', n) else 'No'

