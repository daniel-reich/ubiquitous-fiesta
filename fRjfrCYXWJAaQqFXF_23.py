
def prime_list(n):
  x = 1
  l = []
  while len(l) < n:
    k = []
    for i in range(1,x+1):
      if x%i==0:
        k.append(i)
    if len(k) == 2:
      l.append(x)
    x +=1
  return l
def primorial(n):
  product = 1
  for i in prime_list(n):
    product *= i
  return product

