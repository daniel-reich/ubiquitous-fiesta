
def filter_factorials(numbers):
  return [i for i in numbers if is_factorial(i)]
  
def is_factorial(n):
  t = 1
  for i in range(1, n*2):
    t *= i
    if t == n:
      return True
    if t > n:
      return False

