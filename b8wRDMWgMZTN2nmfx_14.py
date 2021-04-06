
def equal(a, b, c):
  list = [a,b,c]
  if list.count(a) > 1:
    return list.count(a)
  if list.count(b) == 2:
    return 2
  return 0

