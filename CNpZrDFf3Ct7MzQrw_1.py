
def trouble(num1, num2):
  return any(i*2 in str(num2) and i*3 in str(num1) for i in str(num1))

