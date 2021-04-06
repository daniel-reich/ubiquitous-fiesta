
def trouble(num1, num2):
  n1 = str(num1)
  n2 = str(num2)
  for i in '0123456789':
    if 3*i in n1 and 2*i in n2:
      return True
  return False

