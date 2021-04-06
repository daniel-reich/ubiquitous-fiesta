
def math_expr(expr):
  try:
    result = eval(expr)
    return True
  except:
    return False

