
def last(a, n):
  if a == []:
    return 'invalid'
  elif n == 0:
    return []
  elif n > len(a):
    return 'invalid'
  else:
    return a[-n:]

