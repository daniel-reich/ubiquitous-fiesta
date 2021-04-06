
def format_math(expr):
  correct_expr = expr.replace(r'x', '*')
  return "{} = {}".format(expr, round(eval(correct_expr)))

