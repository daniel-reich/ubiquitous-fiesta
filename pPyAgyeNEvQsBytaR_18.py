
def factorial(n):
  nums = range(1, n+1)
  fact = 1
  if n == 0: return 1
  for i in nums:
    fact = fact * i
  return fact

