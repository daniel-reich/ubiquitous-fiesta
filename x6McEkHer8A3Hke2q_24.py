
def factorial(num):
  if (num > 0):
    for i in range(1, num):
      num *= i
    return num
  else:
    return factorial(num)

