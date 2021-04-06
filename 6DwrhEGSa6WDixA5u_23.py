
def is_narcissistic(n):
  if len(str(n)) == 1:
    return True
  elif len(str(n)) == 2:
    return False
  else:
    l = len(str(n))
    s = sum([int(i)**l for i in str(n)])
    return s==n

