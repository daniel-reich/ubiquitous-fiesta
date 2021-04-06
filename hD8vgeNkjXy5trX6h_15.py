
from itertools import permutations
​
def combo(lst, n):
    if n > len(lst):
        return []
    elif n == 0:
        return [[]]
    results = []
    perm = permutations(lst, n)
    for p in perm:
        if sorted(p) not in (sorted(result) for result in results):
            results.append([el for el in p])
    return results

