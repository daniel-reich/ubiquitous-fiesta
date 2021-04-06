
def is_equal(num1, num2):
  if type(num1) == str or type(num2) == str:
    return False
  elif num1 == num2:
    return True
  else:
    return False

