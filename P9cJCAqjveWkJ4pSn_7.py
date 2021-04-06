
def is_equal(num1, num2):
  if isinstance(num1, str) or isinstance(num2, str):
    return False
  else: 
    return num1 == num2

