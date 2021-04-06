
def numbers():
  from itertools import permutations as p
  from random import randint as r
  
  perms = list(p(['1','2','3','4','5'], 5))
  
  return int(''.join(perms[r(1, len(perms))]))

