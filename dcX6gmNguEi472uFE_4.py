
def double_factorial(num):
  if num < 2:
    return 1
  return num * double_factorial(num-2)

