
## Use Bitwise Operator (% modulo operator disallowed.)
def is_odd(n):
  return "Yes" if int(n)&1 else "No"
​
## Use Regular Expression (% modulo operator disallowed.)
import re
def is_even(n):
  return "Yes" if re.match(".*[02468]$",str(n)) else "No"

