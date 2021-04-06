
def eval_algebra(eq):
    ab, c = eq.split(' = ')
    a, op, b = ab.split()
    if c == 'x':
        return eval(a + op + b)
    if a == 'x':
        if op == '+':
            return eval(c + '-' + b)
        else:
            return eval(c + '+' + b)
    if op == '+':
        return eval(c + '-' + a)
    else:
        return eval(a + '-' + c)

