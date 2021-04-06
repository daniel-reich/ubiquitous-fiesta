
def kempner(n):
  def factorial(n):
    if n == 1: return 1
    return n * factorial(n-1)
  for i in range(1, n+1):
    if factorial(i) % n == 0: return i

