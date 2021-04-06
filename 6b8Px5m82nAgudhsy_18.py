
from itertools import permutations
def next_number(num):
  perms = list(set([int("".join(list(y))) for y in permutations([x for x in str(num)])]))
  perms.sort()
  found = perms.index(num)
  if found == len(perms)-1 or perms[-1] == num:
    return perms[found]
  else:
    return perms[found+1]

