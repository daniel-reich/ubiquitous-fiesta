
from itertools import combinations_with_replacement, permutations
def countdown(operands, target):
    ops = ['+', '-', '*', '//']
    n_ops = len(operands) - 1
    for p_oper in permutations(operands):
        for comb in combinations_with_replacement(ops, n_ops):
            for p_ops in permutations(comb):
                res = ''
                for i in range(n_ops):
                    res += str(p_oper[i]) + p_ops[i]
                res += str(p_oper[-1])
                if eval(res) == target:
                    return res
    return ''

