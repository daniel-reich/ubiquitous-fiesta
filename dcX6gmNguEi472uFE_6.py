
def double_factorial(num):
  if num == 2 or num == 1:
    return num
  elif num <= 0:
    return 1
  else:
    return num * double_factorial(num-2)

