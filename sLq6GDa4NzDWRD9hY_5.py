
def count(n):
  l = 1
  if n <= 0:
    n = -n
    for i in (10,100,1000,10000,100000,1000000,10000000,100000000):
      if n / i >= 1:
        l += 1
    return l
  else:
    for i in (10,100,1000,10000,100000,1000000,10000000,100000000):
      if n / i >= 1:
        l += 1
    return l

