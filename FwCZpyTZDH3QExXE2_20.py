
def amount_fib(n):
  if n < 2: return n
  count = 3 
  a, b = 1, 1
  while b < n:
    a, b = b, a + b
    count += 1
  return count - 1

