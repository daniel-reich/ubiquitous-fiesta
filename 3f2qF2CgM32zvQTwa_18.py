
def format_math(expr):
  temp = expr.replace("x","*")
  result = "{} = {}".format(expr,str(int(eval(temp))))
  return result

