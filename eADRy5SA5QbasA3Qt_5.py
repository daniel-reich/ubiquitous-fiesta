
def is_harshad(n):
  x = 0
  m = n
  while m > 0:
    x = x +  m % 10
    m = m // 10
  return not n % x

