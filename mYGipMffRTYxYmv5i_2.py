
def simple_equation(a, b, c):
    for op in ['+', '-', '*', '//']:
        term = str(a) + op + str(b)
        if eval(term) == c:
            eq = term + "=" + str(c)
            return eq.replace('//', '/')
    return ""

