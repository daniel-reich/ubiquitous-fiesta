
def mathematical_function(mathfunc, numbers):
    f, expr = mathfunc.split('=')
    expr = expr.replace('x', '*').replace('^', '**')
    return ['f({})={}'.format(n, round(eval(expr, {'y': n}))) for n in numbers]

