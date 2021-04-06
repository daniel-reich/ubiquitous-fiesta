
def has_consecutive_series(lst1, lst2):
    l1, l2 = len(lst1), len(lst2)
    max_len = max(l1, l2)
    lst1 += [0] * (max_len - l1)
    lst2 += [0] * (max_len - l2)
    total = sum(lst1) + sum(lst2)
    if not 2 * total % max_len:
        tmp = 2 * total // max_len + 1 - max_len
        if not tmp % 2:
            begin = tmp // 2
            while lst1 and lst2:
                pair_found = False
                for i, x in enumerate(lst1):
                    for j, y in enumerate(lst2):
                        if x + y == begin:
                            pair_found = True
                            lst1.pop(i)
                            lst2.pop(j)
                            begin += 1
                            break
                    if pair_found:
                        break
                if not pair_found:
                    return False
            return True
    return False
​
""" Another solution that runs for 4 minutes
from itertools import permutations
def has_consecutive_series(lst1, lst2):
    l1, l2 = len(lst1), len(lst2)
    max_len = max(l1, l2)
    lst1 += [0] * (max_len - l1)
    lst2 += [0] * (max_len - l2)
    for p in permutations(lst1):
        lst = sorted([a + b for a, b in zip(p, lst2)])
        if all(y - x == 1 for x, y in zip(lst, lst[1:])):
            return True
    return False
​
"""

