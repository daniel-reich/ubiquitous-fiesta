
def digit_sum(n):
  ds = 0
  while n > 0:
    ds += (n % 10)
    n //= 10
  return ds
  
def is_equal(lst):
  return digit_sum(lst[0]) == digit_sum(lst[1])

