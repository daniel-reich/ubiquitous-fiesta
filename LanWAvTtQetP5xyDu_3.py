
from itertools import accumulate, permutations
def coins_div(lst):
  s = sum(lst)
  if s%3:
    return False
  else:
    p = {s//3, 2*(s//3), 3*(s//3)}
    return any(p <= set(accumulate(x)) for x in permutations(lst))

