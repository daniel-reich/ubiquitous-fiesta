
def catch_zero_division(expr):
  try:
    if eval(expr) >= 0:
      return False
  except:
    return True

