
def will_hit(equation, position):
  e = equation.replace('x', '*{}'.format(position[0])).replace('y', str(position[1])).replace('=','==')
  return eval(e)

