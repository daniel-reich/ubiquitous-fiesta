
def amount_fib(n):
  a, b = 0, 1
  count = 0
  while a < n:
    a, b = b, a + b
    count += 1
  return count

