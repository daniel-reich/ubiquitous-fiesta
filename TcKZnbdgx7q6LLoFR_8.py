
def collect(s, n, arr=[]):
  if len(s) < n: 
    return []
  return sorted([s[:n]] + collect(s[n:], n))

