
def happy(n):
  tot = 0
  while n:
    n,r = divmod(n,10)
    tot += r**2
  if tot == 4:
    return False
  elif tot == 1:
    return True
  return happy(tot)

