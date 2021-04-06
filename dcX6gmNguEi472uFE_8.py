
def double_factorial(num):
  if not num or num==-1:
    return 1
  return num*double_factorial(num-2)

