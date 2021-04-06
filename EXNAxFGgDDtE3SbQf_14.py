
def shuffle_count(n, r=None, k=None):
  if r is None: r, k = list(range(1, n+1)), 0
  r = sum(([x, y] for x, y in zip(r[:n//2], r[n//2:])), [])
  return k+1 if list(range(1, n+1)) == r else shuffle_count(n, r, k+1)

