
def greater_permutation(expr, nums):
    a, b, c = nums
    perms = ((a, b, c), (a, c, b), (b, a, c), 
             (b, c, a), (c, a, b), (c, b, a))
​
    for i in 'abc':
        expr = expr.replace(i, '{}')
​
    calcs = [(round(eval(expr.format(*p)), 2), expr.format(*p)) for p in perms]
    best = '{} = {}'.format(*reversed(max(calcs)))
    
    if best.endswith('.0'):
        best = best.replace('.0', '')
    return best

