
def will_hit(equation, position):
  m = int(equation.split('x')[0].split('= ')[1])
  b = int(equation.split('x ')[1].replace(' ','').replace('+',''))
  return position[1] == m*position[0] + b

