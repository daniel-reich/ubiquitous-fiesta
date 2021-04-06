
from itertools import groupby
​
def trouble(num1, num2):
  tripled = set(k for k, g in groupby(str(num1)) if len(list(g)) >= 3)
  return any(n * 2 in str(num2) for n in tripled)

