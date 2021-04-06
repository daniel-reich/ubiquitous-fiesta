
def amount_fib(n):
  if n < 2:
    return n
  a, b = 0, 1
  for i in range(3, 166):
    a, b = b, a + b
    if a + b >= n:
      break
  return i

