
def catch_zero_division(expr):
  try:
    if eval(expr) <=0 or eval(expr) >0:
      return False
  except:
    if ZeroDivisionError:
      return True

