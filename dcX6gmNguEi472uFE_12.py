
def factorial(num):
  fact = 1
  while num > 0:
    fact = fact*num
    num -= 2
  return fact
def double_factorial(num):
  print(num)
  if num == 0 or num == 1 or num == -1:
    return 1
  else:
    return num * factorial(num-2)

