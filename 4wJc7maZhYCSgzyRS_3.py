
def two_product(l,n):
  for x in l:
    if n/x in l and l.index(x)>l.index(n/x):
      return[n/x,x]

