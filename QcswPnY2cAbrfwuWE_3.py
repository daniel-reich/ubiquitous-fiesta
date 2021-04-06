
def is_factorial(n):
  i=1
  while True:
    if n%i==0:
      n /= i
      i+=1
    else: return n==1
​
def filter_factorials(numbers):
  return [n for n in numbers if is_factorial(n)]

