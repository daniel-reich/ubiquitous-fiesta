
def collatz(n, r=[]):
  if not r: r = [n]
  if n == 1: return (len(r), max(*r))
  n = n * 3 + 1 if n & 1 else n // 2
  return collatz(n, r + [n])

