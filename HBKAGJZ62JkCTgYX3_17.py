
def last(a, n):
  c = len(a) - n
  if n == 0:
    return []
  elif n > len(a):
    return 'invalid'
  else:
    return a[c:len(a)]

