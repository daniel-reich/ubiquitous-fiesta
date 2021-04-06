
def will_hit(equation, position):
  return position[1] == eval(equation[4:].replace("x", "*" + str(position[0])))

