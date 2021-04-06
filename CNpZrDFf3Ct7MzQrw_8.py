
def trouble(num1, num2):
  for digit in set(str(num1)).union(set(str(num2))):
    if digit*3 in str(num1) and digit*2 in str(num2):
      return True
  return False

