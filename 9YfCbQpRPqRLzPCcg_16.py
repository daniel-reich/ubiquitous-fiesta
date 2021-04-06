
def will_hit(equation, position):
  x = str(position[0])
  y = str(position[1])
  equation = equation.replace('y', y)
  x = '*'+ x
  equation = equation.replace('x',x)
  print(equation)
  eq = equation.split('=')
  return eval(eq[0])==eval(eq[1])

