
def collatz(n):
  c, m = 0, n
  while n > 1:
    n = n * 3 + 1 if n % 2 else n // 2
    c += 1
    m = max(m, n)
  return [c, m]

