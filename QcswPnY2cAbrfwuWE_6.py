
def filter_factorials(numbers):
  factorial = lambda x: 1 if x == 1 else x * factorial(x-1)
  i = 1
  ans = []
  while factorial(i) <= max(numbers):
    if factorial(i) in numbers: ans.append(factorial(i))
    i += 1
  return ans

