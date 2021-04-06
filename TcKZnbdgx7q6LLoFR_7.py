
def collect(s, n):
  # your recursive solution here
  if len(s)<n:
    return []
  else:
    if len(s)==n:
      return [s]
    else:
      return sorted([s[:n]]+collect(s[n:], n))

