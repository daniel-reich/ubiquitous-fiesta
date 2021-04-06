
def catch_zero_division(e):
  try:eval(e);return False
  except ZeroDivisionError:return True

