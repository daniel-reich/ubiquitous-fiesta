
def factorial(num,sum = 1):
  if num == 1:
    return sum
  sum *= num
  return factorial(num-1,sum)

