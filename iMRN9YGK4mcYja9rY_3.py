
def accumulating_product(l):
  for i in range(len(l)-1):
    l[i+1]*=l[i]
  return l

