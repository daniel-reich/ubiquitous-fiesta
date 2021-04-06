
def will_hit(equation, position):
  sides = equation.replace(' ', '').split("=")
  mb = sides[1].split('x')
  m = int(mb[0].strip())
  b = int(mb[1].strip())
  return position[1] == m * position[0] + b

