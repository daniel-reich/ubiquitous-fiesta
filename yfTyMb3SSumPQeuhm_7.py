
def fibonacci(n):
  def fib(n):
    if n == 0:
      return 0, 1
    u, v = fib(n >> 1)
    q = (n & 2) - 1
    u *= u
    v *= v
    if (n & 1):
      return u + v, 3*v - 2*(u - q)
    return 2*(v + q) - 3*u, u + v
  u, v = fib(n >> 1)
  l = 2*v - u
  if (n & 1):
    q = (n & 2) - 1
    return v * l + q
  return u * l

