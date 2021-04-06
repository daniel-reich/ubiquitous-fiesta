
def is_simple(n):
  return n == sum(int(d)**i for i, d in enumerate(str(n), 1))
​
def simple_numbers(a, b):
  return [n for n in range(a, b+1) if is_simple(n)]

