
def will_hit(equation, position):
    x, y = map(str, position)
    return eval(equation.replace('=', '==').replace('y', y).replace('x', '*' + x))

