
def collect(s, n):
  return [] if len(s)<n else sorted([s[:n]] + collect(s[n:], n))

