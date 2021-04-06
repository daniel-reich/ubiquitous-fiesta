
def equal(a, b, c):
  lst = [a, b, c]
  if lst.count(a) >= 2:
    return lst.count(a)
  elif lst.count(b) >=2:
    return lst.count(b)
  elif lst.count(c) >= 2:
    return lst.count(c)
  else:
    return 0

