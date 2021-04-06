
from itertools import permutations
​
def is_vampire(n):
    perm = [''.join(x) for x in permutations(str(n))]
    ln = len(str(n))
    prod = [int(p[x:]) * int(p[:x]) for x in range(1, ln) for p in perm]
    result = 'Pseudovampire' if ln % 2 else 'True Vampire'
    return result if n > 100 and n in prod else 'Normal Number'

