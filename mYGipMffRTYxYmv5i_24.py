
def simple_equation(a, b, c):
    s = 'aopb==c'
    s = s.replace('a', str(a))
    s = s.replace('b', str(b))
    s = s.replace('c', str(c))
    for op in ('+-*/'):
        x = s.replace('op', op)
        if eval(x):
            return x.replace('==', '=')
    return ''

