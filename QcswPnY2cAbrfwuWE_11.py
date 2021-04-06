
def iF(num):
  n = 1
  for i in range(1,10000):
    n *= i
    if n >= num:
      return n == num
​
def filter_factorials(numbers):
  return [n for n in numbers if iF(n)]

