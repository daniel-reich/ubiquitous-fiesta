
def double_factorial(num):
  if num <= 0:
    return 1
  elif num <= 2:
    return num
  else:
    return double_factorial(num - 2) * num

