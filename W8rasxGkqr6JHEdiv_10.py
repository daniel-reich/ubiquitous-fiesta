
from itertools import permutations as perm, combinations_with_replacement as comb
def merge(lst1, lst2):
    rtn = []
    for i in range(max(len(lst1), len(lst2))):
        if i < len(lst1): rtn.append(lst1[i])
        if i < len(lst2): rtn.append(lst2[i])
    return rtn
​
def countdown(operands, target):
    for trial in perm(range(len(operands))):
        for cmb in comb(['+','-','*','//'], len(operands) - 1):
            for ops in set(perm(cmb)):
                expr = " ".join(merge([str(operands[i]) for i in trial], list(ops) + ['']))
                res = eval(expr)
                if res == target:
                    return expr
    return '0'

