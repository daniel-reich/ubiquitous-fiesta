
def catch_zero_division(expr):
  try:
    eval(expr)
  except:
    return True
  else:
    return False

