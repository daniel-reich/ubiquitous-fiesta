
def factorial(num):
  ans = 1
  if num == 0:
    return ans
  else:
    for i in range(num):
      ans *= i+1
  return ans

