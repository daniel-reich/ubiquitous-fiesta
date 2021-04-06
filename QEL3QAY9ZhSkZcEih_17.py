
import re
​
## Use Bitwise Operator (% modulo operator disallowed.)
def is_odd(n):
  return ('No', 'Yes')[n & 1]
    
## Use Regular Expression (% modulo operator disallowed.)
def is_even(n):
  return ('No', 'Yes')[bool(re.search(r'[02468]$', n))]

