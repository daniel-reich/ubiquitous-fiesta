
def catch_zero_division(expr):
  try:
    eval(expr)
    return False
  except:
    return True

