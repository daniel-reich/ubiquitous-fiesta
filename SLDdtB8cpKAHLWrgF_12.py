
import itertools as it
def greater_permutation(expr, nums):
    res = [0, 0, 0, -1000]
    orig = expr
    for x in it.permutations(nums):
        expr = expr.replace('a', str(x[0]))
        expr = expr.replace('b', str(x[1]))
        expr = expr.replace('c', str(x[2]))
        value = round(eval(expr), 2)
        s = str(value).rstrip('0').rstrip('.')
        value = float(value) if s.find('.') != -1 else int(value)
        if value > res[3]:
            res = [x[0], x[1], x[2], value]
        expr = orig
    expr = expr.replace('a', str(res[0]))
    expr = expr.replace('b', str(res[1]))
    expr = expr.replace('c', str(res[2]))
    expr += ' = ' + str(res[3])
    return expr

