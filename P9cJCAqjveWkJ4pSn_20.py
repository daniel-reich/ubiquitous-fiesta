
def is_equal(num1, num2):
  if isinstance(num1, int) and isinstance(num2, int):
    return num1 is num2
  else:
    return False

