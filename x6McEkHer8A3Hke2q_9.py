
def factorial(num):
  if num == 0:
    return 1
  if num == 1:
    return num
  else:
    return num * factorial(num-1)

