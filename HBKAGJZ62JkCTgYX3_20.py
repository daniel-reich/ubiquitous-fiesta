
def last(a, n):
  if n > len(a):
    return 'invalid'
  elif n == 0:
    return []
  else:
    return a[-n:]

