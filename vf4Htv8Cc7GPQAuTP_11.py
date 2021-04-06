
def list_operation(x, y, n):
  numbers = list(range(x,y+1))
  divisors = [i for i in numbers if i % n == 0]
  return divisors

