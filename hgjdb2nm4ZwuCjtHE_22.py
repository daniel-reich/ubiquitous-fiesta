
def math_expr(expr):
  try:
    return type(eval(expr))==int
  except:
    return False

