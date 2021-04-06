
import itertools
​
normal = "Normal Number"
vampire = "True Vampire"
pseudo = "Pseudovampire"
​
def is_vampire(n):
    if n < 100:
        return normal
    digits = [d for d in str(n)]
    L = len(digits)
    k = L // 2
    for perm in itertools.permutations(digits):
        n1 = int(''.join(perm[:k]))
        n2 = int(''.join(perm[k:]))
        if n == n1 * n2:
            return vampire if L % 2 == 0 else pseudo
    return normal

