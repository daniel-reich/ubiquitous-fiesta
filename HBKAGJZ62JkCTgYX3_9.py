
def last(a, n):
  if n > len(a):
    return "invalid"
  if n == 0:
    return []
  return a[-n:]

