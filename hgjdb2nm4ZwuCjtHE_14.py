
def math_expr(expr):
  try:
    eval(expr)
  except:
    return False
  return True

