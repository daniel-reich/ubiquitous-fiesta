
def num_sum(num):
  return sum(map(int, str(num)))
def prod(lst):
  p = 1
  for num in lst:
    p *= num
  return p
def mubashir_function(a, b):
  return prod(map(num_sum, [a, b]))

