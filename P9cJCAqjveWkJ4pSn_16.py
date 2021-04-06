
def is_equal(num1, num2):
  if num1 != num2 :
    return False
  elif isinstance(num1,str) or isinstance(num2,str) :
    return False
  else:
    return True

