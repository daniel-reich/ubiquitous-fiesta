
def collect(s, n, k=None):
  return collect(s, n, []) if k is None else \
    collect(s[n:], n, k+[s[:n]]) if len(s) >= n else sorted(k)

