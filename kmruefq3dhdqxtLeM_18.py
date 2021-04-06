
def digit_sum(k):
  s = 0
  while k > 0:
    s += k % 10
    k //= 10
  return s
  
def sum_digits(a, b):
  return sum([digit_sum(k) for k in range(a, b + 1)])

