
def fact(n):
  if n ==0:
    return 1
  else:
    return n*fact(n-1)
def kempner(n, i = 1):
  if fact(i) % n == 0:
    return i
  else:
    return kempner(n, i+1)

