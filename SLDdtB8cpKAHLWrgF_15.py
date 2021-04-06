
import itertools
​
def greater_permutation(expr, nums):
    max_res = -2**31
    for perm in itertools.permutations(nums):
        a, b, c = [str(_) for _ in perm]
        expr2 = expr.replace('a', a).replace('b', b).replace('c', c)
        res = eval(expr2)
        if res > max_res:
            max_res = res
            A, B, C = a, b, c
    ans = expr.replace('a', A).replace('b', B).replace('c', C) + " = "
    res = str(max_res)
    if '.' not in res:
        ans += res
    else:
        r = float(res)
        if abs(r - int(r)) < 1e-5:
            ans += str(int(round(float(res), 0)))
        else:
            ans += str(round(float(res), 2))
    return ans

