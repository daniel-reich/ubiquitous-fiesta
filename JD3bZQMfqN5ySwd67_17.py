
from itertools import permutations
​
​
def is_vampire(n):
    if n < 99:
        return 'Normal Number'
    perms = set(permutations(str(n)))
    perms = [i if i[0] != '0' and i[len(str(n))//2] != '0' else None for i in perms]
    if len(str(n)) % 2 == 0:
        a = []
        for val in perms:
            if val is not None:
                a.append("{} * {}".format(''.join(val[len(val) // 2:]), ''.join(val[:len(val) // 2])))
        for i in a:
            if eval(i) == n:
                return 'True Vampire'
        return 'Normal Number'
    a = []
    for val in perms:
        if val is not None:
            a.append("{} * {}".format(''.join(val[len(val) // 2 + 1:]), ''.join(val[:len(val) // 2 + 1])))
    for i in a:
        if eval(i) == n:
            return 'Pseudovampire'
    return 'Normal Number'

