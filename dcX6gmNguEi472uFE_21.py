
def double_factorial(num):
  nums = [i for i in range(num, 0, -2)]
  result = 1
  for i in nums:
    result *= i
  return result

