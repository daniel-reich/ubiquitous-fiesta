
from itertools import permutations
def is_vampire(n):
    if n >= 100:
        lp = len(str(n))//2
        if any([int(''.join(p[0:lp])) * int(''.join(p[lp:])) == n for p in permutations(str(n))]):
            return "Pseudovampire" if len(str(n))%2 else "True Vampire"
    return "Normal Number"

