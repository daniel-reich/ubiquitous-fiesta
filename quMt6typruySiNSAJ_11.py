
def shuffle_count(n, r=None, k=None):
  if r is None: k, r = 0, list(range(1, n+1))
  a, b, r, k = r[:n//2], r[n//2:], [], k + 1
  for x, y in zip(a, b): r += [x, y]
  return k if r == list(range(1, n+1)) else shuffle_count(n, r, k)

