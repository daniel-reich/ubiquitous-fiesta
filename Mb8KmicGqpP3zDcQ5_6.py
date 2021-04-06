
def josephus(n, i):
  n = list(range(1, n+1))
  ix = 0
  while len(n) > 1:
    ix += i - 1
    if ix >= len(n): ix -= (ix // len(n)) * len(n)
    n.pop(ix)
  return int(n[0])

