
from itertools import combinations_with_replacement
​
def darts_solver(sections, darts, target):
    cwr = []; res = []
    for i in combinations_with_replacement(sections, darts):
        if sum(i) == target:
            cwr.append(str(i))
​
    for i in cwr:
        i = i.strip('()')
        i = i.replace(', ', '-')
        res.append(i)
    return res

