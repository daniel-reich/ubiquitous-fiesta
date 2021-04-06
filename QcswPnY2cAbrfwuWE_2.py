
def is_factorial(n):
  m, i = 1, 2
  while m < n:
    m *= i
    i += 1
  return m == n
​
def filter_factorials(numbers):
  return list(filter(is_factorial, numbers))

