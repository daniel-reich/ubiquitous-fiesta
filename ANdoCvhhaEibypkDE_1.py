
from itertools import zip_longest
​
def closing_in_sum(n):
  s = str(n)
  half = len(s) // 2
  return sum(
    int(i + j)
    for i, j in zip_longest(s[:half], s[half:], fillvalue='0')
  )

