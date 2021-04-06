
import re
​
def is_odd(n):
  return "Yes" if n^1==n-1 else "No"
​
def is_even(n):
  return "Yes" if re.search("[13579]$", n) is None else "No"

