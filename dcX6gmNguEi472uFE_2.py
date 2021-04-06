
def double_factorial(num):
  if num == 0 or num == -1:
    return 1
  else:
    return num * double_factorial(num - 2)

