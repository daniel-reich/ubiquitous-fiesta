
def will_hit(equation, position):
    x,y=position
    equation=equation[0:equation.find  ("=")]+ "=" + equation[equation.find("="):]
    equation = equation[:equation.find("x")] + '*' + equation[equation.find('x'):]
​
    return eval(equation)

