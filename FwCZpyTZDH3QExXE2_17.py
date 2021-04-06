
fib = [0, 1]
a, b = 0, 1
for _ in range(200):
  a, b = b, a + b
  fib.append(b)
  
def amount_fib(n):
  return len([f for f in fib if f < n])

