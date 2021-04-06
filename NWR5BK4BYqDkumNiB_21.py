
from numpy import prod
​
def digital_division(n):
  i, d = 0, [int(d) for d in str(n)]
​
  if all(n % m == 0 for m in d if m):
    i += 1
  if n % sum(d) == 0:
    i += 1
  if prod(d) and n % prod(d) == 0:
    i += 1
​
  return ["Indivisible", 1, 2, "Perfect"][i]

