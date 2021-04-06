
def double_factorial(num):
  return num * double_factorial(num-2) if num > 0 else 1

