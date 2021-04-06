
def will_hit(equation, position):
  equation = equation[4:].replace('x','*x')
  x, y = position
  return y == eval(equation)

