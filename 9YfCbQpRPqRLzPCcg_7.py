
def will_hit(equation, position):
 equation = equation[:equation.index('x')] + '*' + equation[equation.index('x'):]
 return eval(equation.replace('x',str(position[0])).replace('y',str(position[1])).replace('=', '=='))

