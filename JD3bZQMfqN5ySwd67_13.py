
from itertools import permutations
​
def is_vampire(n):
  if n < 100: return "Normal Number"
  s = str(n)
  p = permutations(s)
  l = len(s) // 2
  v = any(int(''.join(x[:l])) * int(''.join(x[l:])) == n for x in p)
  if not v:
    return "Normal Number"
  elif len(s) % 2:
    return "Pseudovampire"
  return "True Vampire"

