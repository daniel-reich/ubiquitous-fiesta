
def next_number(num):
  from itertools import permutations
  if len(str(num))==1:  return num
  perms = [int(''.join(p)) for p in permutations(str(num))]
  p = sorted([x for x in set(perms)])
  return num if num==max(p) else p[p.index(num)+1]

