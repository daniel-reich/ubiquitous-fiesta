
from itertools import permutations as perms
​
def prod(digits, pivot):
    return int(digits[:pivot])*int(digits[pivot:])
​
def _is_vampire(n):
    pivs = [len(str(n))//2]
    if n%2 == 0: pivs.append(pivs[0] +1)
    return any(prod(''.join(p), i) == n for p in perms(str(n)) for i in pivs)
​
def is_vampire(n):
    if n<100 or not _is_vampire(n):
        return 'Normal Number'
    return 'Pseudovampire' if len(str(n))%2 else 'True Vampire'

