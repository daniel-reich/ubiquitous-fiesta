
from itertools import permutations
def is_vampire(n):
  if n < 100:
    return 'Normal Number'
  n = str(n)
  lst = [i for i in n]
  perm = [list(p) for p in permutations(lst,len(lst))]
  if len(n)%2==0:
    for i in perm:
      a,b = int(''.join(i[:len(n)//2])),int(''.join(i[len(n)//2:]))
      if str(a*b)==n:
        return 'True Vampire'
  else:
    for i in perm:
      a,b = int(''.join(i[:len(n)//2])),int(''.join(i[len(n)//2:]))
      if str(a*b)==n:
        return 'Pseudovampire'
    for i in perm:
      a,b = int(''.join(i[:(len(n)//2)+1])),int(''.join(i[(len(n)//2)+1:]))
      if str(a*b)==n:
        return 'Pseudovampire'
  return 'Normal Number'

