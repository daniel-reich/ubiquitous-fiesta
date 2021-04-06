
def simple_numbers(a, b):
  return list(filter(is_simple, range(a, b+1)))
  
def is_simple(n):
  a = str(n)
  return n == sum(int(i)**int(idx) for idx, i in enumerate(a, 1))

