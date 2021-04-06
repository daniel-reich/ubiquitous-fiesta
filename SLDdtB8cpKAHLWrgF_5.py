
from itertools import permutations
​
def evaluated(expr, a, b, c):
    for char, var in [('a', a), ('b', b), ('c', c)]:
        expr = expr.replace(char, str(var))
    value = str(round(eval(expr),2)).rstrip('0').rstrip('.') or '0'
    return '{} = {}'.format(expr, value)
​
def greater_permutation(expr, nums):
    evaluations = (evaluated(expr, a, b, c) for a,b,c in permutations(nums))
    return max(evaluations, key=lambda x: float(x.split('=')[1]))

