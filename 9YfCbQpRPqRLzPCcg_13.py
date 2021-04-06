
def will_hit(equation, position):
  x,y = position
  b = int(equation[-3:].replace(" ", ""))
  m = int(equation.split("x")[0][-2:].replace(" ", ""))
  return  y == m*x + b

