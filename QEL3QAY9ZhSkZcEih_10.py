
import re
## Use Bitwise Operator (% modulo operator disallowed.)
def is_odd(n):
  binary = "{0:b}".format(n)
  if binary[-1] == '1':
    return "Yes"
  else:
    return "No"
​
## Use Regular Expression (% modulo operator disallowed.)
def is_even(n):
  n = list(n)
  pattern = re.compile(r'[13579]')
  res = re.search(pattern, n[-1])
  if res:
    return "No"
  else:
    return "Yes"

