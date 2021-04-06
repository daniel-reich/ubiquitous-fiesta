
def trouble(num1, num2):
  for i in "0123456789":
    if i*3 in str(num1) and i*2 in str(num2):
      return True
  return False

