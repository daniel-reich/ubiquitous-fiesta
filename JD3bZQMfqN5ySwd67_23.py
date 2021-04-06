
from itertools import permutations
​
def is_vampire(n):
    if n < 100:
        return 'Normal Number'
    s = str(n)
    for p in permutations(s):
        p = ''.join(p)
        left, right = p[:len(p)//2], p[len(p)//2:]
        if int(left) * int(right) == n:
            return 'Pseudovampire' if len(s)%2 else 'True Vampire'
    return 'Normal Number'

