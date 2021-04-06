
def every_some(test, val, a, b, c, d, e):
    var = (a, b, c, d, e)
    if val == 'everybody':
        return all(eval('{} {}'.format(x, test)) for x in var)
    return any(eval('{} {}'.format(x, test)) for x in var)

