
def will_hit(equation, position):
    p, q = position
    equation = equation.replace('=', '==')
    equation = equation.replace('y', str(q))
    equation = equation.replace('x', '*' + str(p))
    return eval(equation)

