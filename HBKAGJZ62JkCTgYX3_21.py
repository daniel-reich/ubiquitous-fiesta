
def last(a, n):
  if n == 0:
    return []
  elif n > len(a):
    return "invalid"
  elif n <= len(a):
    return a[-n:]

