
def collatz(n):
  c = 0
  maxn = n
  while n > 1:
    if n % 2 == 0: n = n//2
    else: n = 3 * n + 1
    maxn = max(maxn, n)
    c += 1
  return [c, maxn]

