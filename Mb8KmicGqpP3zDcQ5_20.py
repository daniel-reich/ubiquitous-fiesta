
def josephus(n, i):
  r = 0
  l = range(n)
  while len(l) > 1:
    ltmp = []
    for k, j in enumerate(l):
      if (k+1+r)%i != 0:
        ltmp.append(j)
    r = len(l) % i + r
    l = ltmp  
  return l[0] + 1 if l else n

