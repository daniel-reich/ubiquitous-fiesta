
def collect(s, n):
  l = len(s)
  if n > l:
    return []
  return sorted([s[k*n:k*n+n] for k in range(l // n)])

