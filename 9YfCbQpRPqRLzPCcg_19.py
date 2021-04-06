
def will_hit(equation, position):
  x = position[0]
  y = position[1]
  value = equation.strip("y = ")
  equation1 = value.replace("x","*" + str(x))
  y1 = eval(equation1)
  return y == y1

