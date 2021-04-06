
def catch_zero_division(expr):
  try:
    eval(expr);
    return False;
  except ZeroDivisionError:
    return True;

