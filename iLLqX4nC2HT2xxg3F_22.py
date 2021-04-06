
from itertools import accumulate as acc
def deepest(lst):
  return max(acc({r"[":1, r"]":-1}.get(x,0) for x in str(lst)))

