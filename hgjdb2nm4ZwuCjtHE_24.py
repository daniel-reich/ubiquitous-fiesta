
def math_expr(expr):
  try:
    total = eval(expr)
    return True
  except (NameError, ValueError):
    return False

