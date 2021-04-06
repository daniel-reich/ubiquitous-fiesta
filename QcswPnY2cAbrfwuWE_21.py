
def filter_factorials(numbers):
  def factorial(n, i=1):
    return n == 1 or (n%i==0 and factorial(n//i, i+1))
  return [n for n in numbers if factorial(n)]

