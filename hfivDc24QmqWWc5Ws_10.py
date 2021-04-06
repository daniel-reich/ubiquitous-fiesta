
def eratosthenes(num):
  a = list(range(2,num))
  for x in a:
    a[x:] = filter(lambda y: y%x, a[x:])
  return a

