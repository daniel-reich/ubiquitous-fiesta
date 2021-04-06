
def math_expr(expr):
  try:
     eval(expr)
     return True
  except:
    return False

