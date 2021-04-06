
def factorial(num, p=1):
  if num == 0:
    return p
  else:
    p *= num
    return factorial(num-1,p)

