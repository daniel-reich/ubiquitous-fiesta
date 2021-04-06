
def double_factorial(num):
  if num in (0,1) or num < 0:
    return 1
  return num * double_factorial(num-2)

