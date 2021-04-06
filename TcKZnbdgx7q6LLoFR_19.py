
def collect(s, n):
  # your recursive solution here
  if len(s)<n:
    return []
  if len(s)==n:
    return [s]
  return sorted(collect(s[:n],n)+collect(s[n:],n))

