
def collect(s, n):
  # your recursive solution here
  # if the text is too short, cut it
  if len(s) < n:
    return []
  # otherwise, slice the first n and collect the rest
  return sorted([s[:n]] + collect(s[n:], n))

