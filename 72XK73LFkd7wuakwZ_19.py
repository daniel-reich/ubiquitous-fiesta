
def junction_or_self(n):
  s = lambda n: n + sum(int(c) for c in str(n))
  res = [i for i in range(n, 0, -1) if s(i) == n]
  return res if res else "Self"

