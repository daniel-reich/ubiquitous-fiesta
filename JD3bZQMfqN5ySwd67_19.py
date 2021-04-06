
from itertools import permutations
​
def is_vampire(n):
  if n < 100: return 'Normal Number'
  l = len(str(n))
  for i in permutations(str(n)):
    l1, r1 = map(int, (''.join(i[:l//2]), ''.join(i[l//2:])))
    l2, r2 = map(int, (''.join(i[:l//2+l%2]), ''.join(i[l//2+l%2:])))
    if n in (l1*r1, l2*r2):
      return ['True Vampire', 'Pseudovampire'][l%2]
  return 'Normal Number'

