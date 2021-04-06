
import re
​
def is_odd(n):
  return ['No', 'Yes'][n ^ 1 == n - 1]
​
def is_even(n):
  return ['No', 'Yes'][re.search('[02468]$', n) is not None]

