
def trouble(num1, num2):
  i = 0
  while i < 10:
    n1 = str(num1).count(str(i))
    if n1 >= 3 and str(num2).count(str(i)) >= 2:
        return True
    else:
      i += 1
  return False

