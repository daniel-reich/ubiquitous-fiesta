
from fractions import gcd
def is_prim_pyth_triple(lst):
  if sum([i**2 for i in lst if i!=max(lst)]) == max(lst)**2:
    return gcd(lst[0],lst[1]) == 1 and gcd(lst[1],lst[2]) == 1 and gcd(lst[0],lst[2]) == 1
  return False

