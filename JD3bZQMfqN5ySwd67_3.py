
from itertools import permutations as perm
def is_vampire(n):
    ns = str(n)
    sl = len(ns)
    if sl > 2:
        for p in perm(ns, sl):
            if int(''.join(p[:sl//2])) * int(''.join(p[sl//2:])) == n:
                return "Pseudovampire" if sl%2 else "True Vampire"
    return "Normal Number"

