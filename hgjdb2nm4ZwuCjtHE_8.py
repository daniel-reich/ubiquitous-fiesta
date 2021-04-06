
def math_expr(expr):
  try:
    eval(expr)
    return True
  except NameError:
    return False

