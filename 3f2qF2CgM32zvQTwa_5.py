
def format_math(expr):
  return "".join([expr," = ",str(int(eval(expr.replace("x","*"))))])

