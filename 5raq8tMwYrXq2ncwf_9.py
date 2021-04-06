
def catch_zero_division(expr):
  try:
    print(eval(expr))
  except ZeroDivisionError:
    return True
  return False

