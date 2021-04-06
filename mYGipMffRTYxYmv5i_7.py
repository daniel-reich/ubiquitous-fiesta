
def simple_equation(a, b, c):
    '''
    Returns a simple equation linking a and b with c or '' if not possible
    '''
    a, b = str(a), str(b)
    for op in '+-*/':
        if eval(a + op + b) == c:
            return '{}{}{}={}'.format(a, op, b, str(c))
​
    return ''

