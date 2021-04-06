
def format_math(expr):
  expr1=expr.replace("x","*")
  return "{} = {}".format(expr,int(eval(expr1)))

