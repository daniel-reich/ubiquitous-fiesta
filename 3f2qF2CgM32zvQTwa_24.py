
def format_math(expr):
  return expr + " = " + str(int(eval(expr.replace("x","*"))))

