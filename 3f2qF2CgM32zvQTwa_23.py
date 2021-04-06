
def format_math(expr):
  fixed_mult = expr.replace('x', '*')
  return "{} = {:.0f}".format(expr, eval(fixed_mult))

