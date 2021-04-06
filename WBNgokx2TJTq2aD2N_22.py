
def smallest(d, v):
  for x in range(10**(d-1), 10**(d)):
    if not x % v:
      return x

