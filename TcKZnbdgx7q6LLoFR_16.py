
def collect(s, n):
  # your recursive solution here
  if len(s) < n:
    return []
  result = [s[:n]] + [i for i in collect(s[n:], n)]
  result.sort()
  return result

