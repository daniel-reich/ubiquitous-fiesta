
def double_factorial(num):
  return 1 if num < 2 else num * double_factorial(num - 2)

