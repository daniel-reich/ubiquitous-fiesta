
def double_factorial(num):
  factorial = 1
  if num%2==0:
    for i in range(num,0,-2):
      factorial *= i
  else:
    for i in range(num,1,-2):
      factorial *= i
  return factorial

