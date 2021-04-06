
import itertools
​
operations = [' + ', ' - ', ' * ', ' // ']
​
def countdown(operands, target):
    nums = [str(_) for _ in operands]
    n = len(nums)
    for perm_nums in itertools.permutations(nums):
        for comb_ops in itertools.combinations_with_replacement(operations, n-1):
            for perm_ops in itertools.permutations(comb_ops):
                term = ''.join([perm_nums[i] + perm_ops[i] for i in range(n-1)]) + perm_nums[-1]
                if eval(term) == target:
                    return term
    assert False, "We should never reach this point, dummy!"

