
def mathematical(expr, nums):
    res = []
    for y in nums:
        calc = eval(expr[5:].replace('y', str(y)).replace('^', '**').replace('x', '*'))
        res.append('f({})={}'.format(y, int(calc)))
    return res

